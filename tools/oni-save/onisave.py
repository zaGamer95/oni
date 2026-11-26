"""Minimal Oxygen Not Included save reader (Python port of RoboPhred/oni-save-parser's read path).

Usage: python3 -I onisave.py <save.sav>   (prints a structural overview)
"""
import json
import struct
import sys
import zlib


class R:
    def __init__(self, b, pos=0):
        self.b = b
        self.p = pos

    def take(self, n):
        v = self.b[self.p:self.p + n]
        if len(v) != n:
            raise EOFError(f"read {n} at {self.p}")
        self.p += n
        return v

    def u(self, fmt):
        n = struct.calcsize(fmt)
        v = struct.unpack_from("<" + fmt, self.b, self.p)
        self.p += n
        return v[0] if len(v) == 1 else v

    def i32(self): return self.u("i")
    def u32(self): return self.u("I")
    def byte(self): return self.u("B")
    def f32(self): return self.u("f")

    def kstr(self):
        n = self.i32()
        if n < 0:
            return None
        return self.take(n).decode("utf-8", "replace")


# ---- type templates -------------------------------------------------------
VALUE_MASK, IS_VALUE, IS_GENERIC = 63, 64, 128
GENERIC = {18, 19, 20, 21, 0, 22}


def parse_typeinfo(r):
    info = r.byte()
    t = info & VALUE_MASK
    ti = {"info": info, "t": t}
    if t in (0, 13):
        ti["name"] = r.kstr()
    if info & IS_GENERIC:
        n = r.byte()
        ti["sub"] = [parse_typeinfo(r) for _ in range(n)]
    elif t == 17:
        ti["sub"] = [parse_typeinfo(r)]
    return ti


def parse_templates(r):
    out = {}
    for _ in range(r.i32()):
        name = r.kstr()
        nf, np_ = r.i32(), r.i32()
        fields = [(r.kstr(), parse_typeinfo(r)) for _ in range(nf)]
        props = [(r.kstr(), parse_typeinfo(r)) for _ in range(np_)]
        out[name] = fields + props
    return out


class Parser:
    def __init__(self, templates):
        self.T = templates

    def by_template(self, r, name):
        tpl = self.T.get(name)
        if tpl is None:
            raise KeyError(f"template {name!r} not found")
        return {fname: self.by_type(r, ti) for fname, ti in tpl}

    def array_like(self, r, ti):
        el = ti["sub"][0]
        r.i32()  # data length
        n = r.i32()
        if n < 0:
            return None
        et = el["t"]
        if et == 2:
            return bytes(r.take(n))
        if el["info"] & IS_VALUE:
            return [self.by_template(r, el["name"]) for _ in range(n)]
        return [self.by_type(r, el) for _ in range(n)]

    def by_type(self, r, ti):
        t = ti["t"]
        if t in (17, 20, 21, 22):
            return self.array_like(r, ti)
        if t == 3: return bool(r.byte())
        if t == 2: return r.byte()
        if t == 1: return r.u("b")
        if t == 4: return r.u("h")
        if t == 5: return r.u("H")
        if t == 6: return r.i32()
        if t == 7: return r.u32()
        if t == 8: return r.u("q")
        if t == 9: return r.u("Q")
        if t == 10: return r.f32()
        if t == 11: return r.u("d")
        if t == 12: return r.kstr()
        if t == 13: return r.i32()
        if t == 14: return r.u("ii")
        if t == 15: return r.u("ff")
        if t == 16: return r.u("fff")
        if t == 23: return tuple(r.take(4))
        if t == 19:
            kt, vt = ti["sub"]
            r.i32()
            n = r.i32()
            if n < 0:
                return None
            vals = [self.by_type(r, vt) for _ in range(n)]
            keys = [self.by_type(r, kt) for _ in range(n)]
            return list(zip(keys, vals))
        if t == 18:
            if r.i32() >= 0:
                kt, vt = ti["sub"]
                return (self.by_type(r, kt), self.by_type(r, vt))
            return None
        if t == 0:
            ln = r.i32()
            if ln < 0:
                return None
            start = r.p
            name = ti["name"]
            if name in self.T:
                obj = self.by_template(r, name)
            else:
                obj = None
            if r.p - start != ln:
                r.p = start + ln  # tolerate template drift
            return obj
        raise ValueError(f"unknown type code {t}")

    # ---- game objects ------------------------------------------------------
    def modifiers(self, r, inst_type):
        out = []
        for _ in range(r.i32()):
            name = r.kstr()
            ln = r.i32()
            start = r.p
            try:
                v = self.by_template(r, inst_type)
            except Exception:
                v = None
            r.p = start + ln
            out.append((name, v))
        return out

    def game_object(self, r):
        pos = r.u("fff")
        rot = r.u("ffff")
        scale = r.u("fff")
        folder = r.byte()
        behaviors = {}
        order = []
        for _ in range(r.i32()):
            name = r.kstr()
            ln = r.i32()
            start = r.p
            data, extra = None, None
            try:
                data = self.by_template(r, name) if name in self.T else None
                if name == "Storage":
                    items = []
                    for _ in range(r.i32()):
                        iname = r.kstr()
                        go = self.game_object(r)
                        go["name"] = iname
                        items.append(go)
                    extra = items
                elif name == "MinionModifiers":
                    extra = {"amounts": self.modifiers(r, "Klei.AI.AmountInstance"),
                             "sicknesses": self.modifiers(r, "Klei.AI.SicknessInstance")}
                elif name == "Modifiers":
                    extra = {"amounts": self.modifiers(r, "Klei.AI.AmountInstance"),
                             "diseases": self.modifiers(r, "Klei.AI.DiseaseInstance")}
            except Exception as e:  # keep going on template drift
                data = {"_error": str(e)}
            r.p = start + ln
            behaviors[name] = {"data": data, "extra": extra}
            order.append(name)
        return {"pos": pos, "rot": rot, "scale": scale, "folder": folder,
                "behaviors": behaviors, "order": order}

    def game_objects(self, r):
        groups = {}
        for _ in range(r.i32()):
            prefab = r.kstr()
            count = r.i32()
            ln = r.i32()
            start = r.p
            objs = []
            try:
                for _ in range(count):
                    objs.append(self.game_object(r))
            except Exception as e:
                objs.append({"_error": str(e)})
            r.p = start + ln
            groups[prefab] = objs
        return groups


def load(path):
    d = open(path, "rb").read()
    r = R(d)
    build, hsize, hver = r.u32(), r.u32(), r.u32()
    compressed = bool(r.u32()) if hver >= 1 else False
    info = json.loads(r.take(hsize).decode("utf-8"))
    templates = parse_templates(r)
    body = zlib.decompress(d[r.p:]) if compressed else d[r.p:]
    P = Parser(templates)
    b = R(body)
    assert b.kstr() == "world"
    assert b.kstr() == "Klei.SaveFileRoot"
    world = P.by_template(b, "Klei.SaveFileRoot")
    assert b.kstr() == "Game+Settings"
    settings = P.by_template(b, "Game+Settings")
    sim_len = b.i32()
    sim = bytes(b.take(sim_len))
    assert b.take(4) == b"KSAV", "KSAV marker"
    ver = (b.i32(), b.i32())
    groups = P.game_objects(b)
    game_data = None
    try:
        if b.kstr() == "Game+GameSaveData":
            game_data = P.by_template(b, "Game+GameSaveData")
    except Exception as e:
        game_data = {"_error": str(e)}
    return {"game_data": game_data, "build": build, "info": info, "templates": templates, "world": world,
            "settings": settings, "sim": sim, "version": ver, "groups": groups,
            "body": body, "body_rest": b.p}


if __name__ == "__main__":
    s = load(sys.argv[1])
    print("build", s["build"], "version", s["version"], s["info"])
    print("templates", len(s["templates"]))
    w = s["world"]
    print("world keys", {k: (type(v).__name__, len(v) if hasattr(v, "__len__") else v) for k, v in w.items()})
    print("sim bytes", len(s["sim"]))
    for k, v in s["groups"].items():
        err = [o for o in v if "_error" in o]
        print(f"  {k}: {len(v)}" + (f"  ERR {err[0]['_error']}" if err else ""))
