"""Turn an ONI save into a base-state report + per-world maps and data.

Usage: python3 -I oni_report.py <save.sav> <out_dir>
Outputs in out_dir:
  report.md                 human-readable summary (per world)
  colony.json               duplicants, buildings (with cell positions), resources
  world_<id>_grid.npz       per-world cell arrays: element (str id), temp_c, mass_kg, germ, germ_count, biome
  world_<id>_map.png        element map with Abyssalite highlighted and biome borders
"""
import collections
import json
import math
import os
import struct
import sys

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import onisave  # noqa: E402


def sdbm(s, signed=False):
    h = 0
    for ch in s.lower():
        h = (ord(ch) + (h << 6) + (h << 16) - h) & 0xFFFFFFFF
    if signed and h >= 1 << 31:
        h -= 1 << 32
    return h


# Optional extra names: aki-art/oni-ids tables dumped to oni_ids.json (not committed; no license on that repo).
_ids_path = os.path.join(HERE, "oni_ids.json")
IDS = json.load(open(_ids_path, encoding="utf-8")) if os.path.exists(_ids_path) else {"elements": []}
IDS["choregroups"] = [("Attacking", "Combat"), ("Life Support", "LifeSupport"), ("Toggling", "Toggle"),
                      ("Doctoring", "MedicalAid"), ("Rocketry", "Rocketry"), ("Tidying", "Basekeeping"),
                      ("Cooking", "Cook"), ("Decorating", "Art"), ("Researching", "Research"),
                      ("Operating", "MachineOperating"), ("Farming", "Farming"), ("Ranching", "Ranching"),
                      ("Building", "Build"), ("Digging", "Dig"), ("Supplying", "Hauling"), ("Storing", "Storage"),
                      ("Relaxing", "Recreation"), ("Suit Wearing", "Suits")]
IDS["skillgroups"] = [("Digging", "Mining"), ("Building", "Building"), ("Farming", "Farming"),
                      ("Ranching", "Ranching"), ("Cooking", "Cooking"), ("Decorating", "Art"),
                      ("Researching", "Research"), ("Rocketry", "Rocketry"), ("Suit Wearing", "Suits"),
                      ("Supplying", "Hauling"), ("Operating", "Technicals"), ("Doctoring", "MedicalAid"),
                      ("Tidying", "Basekeeping")]
EXTRA_ELEMENTS = """Vacuum Unobtanium Katairite Oxygen ContaminatedOxygen CarbonDioxide Hydrogen Methane ChlorineGas Chlorine
Steam Water DirtyWater SaltWater Brine Ice DirtyIce BrineIce Snow CrushedIce SourGas CrudeOil Petroleum Naphtha Propane
Helium LiquidHelium LiquidHydrogen LiquidOxygen LiquidMethane LiquidCarbonDioxide LiquidSulfur SulfurGas Sulfur Magma
Obsidian IgneousRock SedimentaryRock Granite SandStone Sand Dirt Clay Algae SlimeMold Phosphorite Fertilizer Carbon
RefinedCarbon Cuprite Copper IronOre Iron GoldAmalgam Gold Lead Wolframite Tungsten AluminumOre Aluminum Cobaltite Cobalt
Steel Glass Diamond Fossil Lime Salt BleachStone Rust Regolith MaficRock Isoresin Resin Polypropylene Ceramic Niobium
Ethanol Sucrose Graphite Fallout NuclearWaste Radium UraniumOre EnrichedUranium DepletedUranium Yellowcake ToxicSand
Rock RockGas CarbonGas Creature Electrum Mercury MercuryGas Milk MilkFat ViscoGel SuperCoolant SuperInsulator Tallow
SolidMercury MoltenGlass MoltenCopper MoltenIron MoltenGold MoltenLead MoltenSteel MoltenCarbon MoltenSalt MoltenSucrose
OxyRock PhosphateNodules Brick SolidCarbonDioxide SolidMethane SolidOxygen SolidHydrogen Cinnabar Amber Peat Nickel
NickelOre Iridium MoltenNickel Mud ToxicMud DirtyWaterIce PhytoOil RefinedLipid NaturalResin NaturalResinLiquid
SolidResin Kelp Coral Sap Corallium SolidChlorine""".split()
ELEM = {}
for name, eid in IDS["elements"]:
    ELEM[sdbm(eid)] = eid
for eid in EXTRA_ELEMENTS:
    ELEM.setdefault(sdbm(eid), eid)
GERMS = {sdbm(n): n for n in ["FoodPoisoning", "SlimeLung", "PollenGerms", "ZombieSpores", "RadiationSickness"]}
CHORE = {sdbm(i, True): n for n, i in IDS["choregroups"]}
SKILLGRP = {sdbm(i, True): n for n, i in IDS["skillgroups"]}

GASES = set("""Oxygen ContaminatedOxygen CarbonDioxide Hydrogen Methane ChlorineGas Steam SourGas Propane Helium SulfurGas
RockGas CarbonGas MercuryGas Fallout""".split())
LIQUIDS = set("""Water DirtyWater SaltWater Brine CrudeOil Petroleum Naphtha LiquidHelium LiquidHydrogen LiquidOxygen
LiquidMethane LiquidCarbonDioxide LiquidSulfur Magma Chlorine Ethanol Mercury Milk ViscoGel SuperCoolant MoltenGlass
MoltenCopper MoltenIron MoltenGold MoltenLead MoltenSteel MoltenCarbon MoltenSalt MoltenSucrose NuclearWaste PhytoOil
NaturalResinLiquid Resin MoltenNickel""".split())

KO = {  # 게임 공식 한글 명칭은 확인된 것만. 나머지는 영문 ID 그대로.
    "Katairite": "심성석", "Oxygen": "산소", "ContaminatedOxygen": "오염된 산소", "CarbonDioxide": "이산화탄소",
    "Hydrogen": "수소", "Methane": "천연가스", "Water": "물", "DirtyWater": "오염된 물", "Vacuum": "진공",
    "Unobtanium": "중성자물질", "CrudeOil": "원유", "Petroleum": "석유", "Steam": "증기", "Ice": "얼음",
    "SaltWater": "소금물", "Brine": "염수", "SlimeMold": "는지렁이", "Algae": "조류",
}

def _load_glossary():  # 게임 공식 한국어 원소 이름 (_data/glossary_ko.yml, Klei 번역 파일에서 생성)
    import re as _re
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_data", "glossary_ko.yml")
    out = {}
    try:
        for line in open(path, encoding="utf-8"):
            m = _re.search(r'ko: "([^"]+)".*key: ELEMENTS\.([A-Z0-9_]+)\.NAME', line)
            if m: out[m.group(2)] = m.group(1)
    except OSError:
        pass
    return out
_GL = _load_glossary()
for _eid in set(ELEM.values()) | set(KO):
    if _eid.upper() in _GL: KO[_eid] = _GL[_eid.upper()]
ZONE = ["FrozenWastes", "CrystalCaverns", "BoggyMarsh", "Sandstone", "ToxicJungle", "MagmaCore", "OilField", "Space",
        "Ocean", "Rust", "Forest", "Radioactive", "Swamp", "Wasteland", "RocketInterior", "Metallic", "Barren", "Moo",
        "IceCaves", "CarrotQuarry", "SugarWoods", "PrehistoricGarden", "PrehistoricRaptor", "PrehistoricWetlands"]
ZONE_COLOR = {"Sandstone": (200, 170, 110), "ToxicJungle": (140, 170, 60), "Wasteland": (190, 150, 90),
              "FrozenWastes": (150, 200, 230), "BoggyMarsh": (120, 150, 100), "MagmaCore": (180, 60, 40),
              "OilField": (90, 70, 50), "Space": (20, 20, 40), "Barren": (130, 120, 120), "Swamp": (100, 120, 80),
              "Forest": (90, 140, 70), "Ocean": (60, 110, 170), "Rust": (170, 90, 60), "Radioactive": (120, 200, 80),
              "Metallic": (160, 140, 90), "Moo": (150, 130, 170)}

KCAL = {  # kcal per unit (wiki values; tooltip wins if they differ)
    "MushBar": 800, "BasicPlantFood": 600, "BasicPlantBar": 1700, "PrickleFruit": 1600, "GrilledPrickleFruit": 2000,
    "Salsa": 4400, "Meat": 1600, "CookedMeat": 4000, "FishMeat": 1000, "CookedFish": 1600, "ShellfishMeat": 1000,
    "Mushroom": 2400, "FriedMushroom": 2800, "ColdWheatBread": 1200, "SpiceBread": 4000, "Tofu": 3600,
    "SpicyTofu": 4000, "SurfAndTurf": 6000, "Lettuce": 400, "MushroomWrap": 4800, "FruitCake": 4000,
    "BurgerMeal": 6000, "SwampFruit": 1840, "SwampDelights": 2240, "WormBasicFruit": 800, "WormSuperFruit": 250,
    "WormBasicFood": 1200, "WormSuperFood": 2400, "PlantMeat": 1200, "BerryPie": 4200, "CookedEgg": 2800,
    "RawEgg": 1600, "Pemmican": 2600, "FieldRation": 800, "DeepFriedMeat": 4000, "Sushi": 1600,
    "GammaMush": 1050, "BasicForagePlant": 800, "MushroomPie": 2400, "Curry": 5000, "Quiche": 6400,
}


def ename(h):
    return ELEM.get(h & 0xFFFFFFFF, f"#{h & 0xFFFFFFFF:08x}")


def state(e):
    if e in GASES:
        return "gas"
    if e in LIQUIDS or e.startswith("Molten") or e.startswith("Liquid"):
        return "liquid"
    if e in ("Vacuum",):
        return "vacuum"
    return "solid"


def color(e, m):
    st = state(e)
    if e == "Katairite":
        return (255, 0, 200)
    if e == "Unobtanium":
        return (0, 0, 0)
    if e == "Vacuum":
        return (10, 10, 18)
    if e == "Oxygen":
        return (120, 190, 255)
    if e == "ContaminatedOxygen":
        return (170, 200, 120)
    if e == "CarbonDioxide":
        return (70, 70, 70)
    if e == "Hydrogen":
        return (230, 160, 200)
    if e == "Methane":
        return (230, 200, 120)
    if st == "gas":
        return (160, 160, 200)
    if e in ("Water",):
        return (40, 90, 220)
    if e in ("DirtyWater",):
        return (110, 120, 60)
    if e in ("CrudeOil", "Petroleum"):
        return (60, 40, 20)
    if st == "liquid":
        return (60, 140, 170)
    h = sdbm(e)
    g = 90 + (h % 70)
    return (g, int(g * 0.85), int(g * 0.7))


# ---------------------------------------------------------------------------
def read_sim(sim):
    magic, ver, w, h = struct.unpack_from("<8sIii", sim, 0)
    assert magic == b"SIMSAVE\x00", magic
    n = w * h
    off = 29
    cells = np.frombuffer(sim, dtype=np.dtype([("e", "<u4"), ("t", "<f4"), ("m", "<f4"), ("x", "<u4")]),
                          count=n, offset=off)
    germ = np.frombuffer(sim, dtype=np.dtype([("g", "<u4"), ("c", "<i4")]), count=n, offset=off + 16 * n)
    return w, h, cells.reshape(h, w), germ.reshape(h, w)


def world_list(s):
    out = []
    for a in s["groups"].get("Asteroid", []):
        w = a["behaviors"]["WorldContainer"]["data"]
        out.append({"id": w["id"], "worldName": w["worldName"].split("/")[-1], "offset": w["worldOffset"],
                    "size": w["worldSize"], "start": w["isStartWorld"], "visited": w["isDupeVisited"],
                    "storyTraits": [t.split("/")[-1] for t in (w["m_storyTraitIds"] or [])],
                    "subworlds": w["m_subworldNames"] or []})
    return out


def world_of(worlds, x, y):
    for w in worlds:
        ox, oy = w["offset"]
        sx, sy = w["size"]
        if ox <= x < ox + sx and oy <= y < oy + sy:
            return w["id"]
    return None


def is_building(o):
    return "BuildingComplete" in o.get("behaviors", {})


def prim(o):
    pe = o.get("behaviors", {}).get("PrimaryElement", {}).get("data") or {}
    return pe


def walk_items(s):
    """Yield (prefab, obj, container_prefab or None, x, y) for every loose or stored object."""
    for prefab, objs in s["groups"].items():
        for o in objs:
            if "_error" in o:
                continue
            x, y = o["pos"][0], o["pos"][1]
            yield prefab, o, None, x, y
            st = o["behaviors"].get("Storage")
            if st and st["extra"]:
                for it in st["extra"]:
                    yield it["name"], it, prefab, x, y


def duplicants(s, worlds):
    out = []
    for m in s["groups"].get("Minion", []):
        b = m["behaviors"]
        ident = b["MinionIdentity"]["data"]
        res = b["MinionResume"]["data"]
        attrs = {a["attributeId"]: a["level"] for a in b["Klei.AI.AttributeLevels"]["data"]["saveLoadLevels"]}
        amounts = dict(b["MinionModifiers"]["extra"]["amounts"])
        mastered = [k for k, v in res["MasteryBySkillID"] if v]
        granted = res["GrantedSkillIDs"] or []
        xp = res["totalExperienceGained"]
        # MinionResume.CalculateTotalSkillPointsGained (TUNING.SKILLS: 15 pts over 250 cycles, power 1.44)
        pts = int(math.floor(math.pow(xp / 600.0 / 250.0, 1 / 1.44) * 15)) if xp > 0 else 0
        spent = len([k for k in mastered if k not in granted])
        prio = {CHORE.get(h["hash"], h["hash"]): p["priority"]
                for h, p in b["ChoreConsumer"]["data"]["choreGroupPriorities"]}
        x, y = m["pos"][0], m["pos"][1]
        out.append({
            "name": ident["name"], "world": world_of(worlds, x, y), "cell": [int(x), int(y)],
            "traits": b["Klei.AI.Traits"]["data"]["TraitIds"],
            "interests": [SKILLGRP.get(h["hash"], h["hash"]) for h, v in res["AptitudeBySkillGroup"] if v > 0],
            "attributes": {k: v for k, v in attrs.items() if v},
            "skills": mastered, "skill_points_est": pts, "unspent_points_est": pts - spent,
            "hat": res["currentHat"],
            "stress": round(amounts.get("Stress", {}).get("value", 0), 1),
            "kcal": round(amounts.get("Calories", {}).get("value", 0) / 1000),
            "hp": amounts.get("HitPoints", {}).get("value"),
            "bladder": round(amounts.get("Bladder", {}).get("value", 0)),
            "stamina": round(amounts.get("Stamina", {}).get("value", 0)),
            "germs": {k: v["value"] for k, v in amounts.items() if k in GERMS.values() and v["value"]},
            "sick": [n for n, _ in b["MinionModifiers"]["extra"]["sicknesses"]],
            "effects": [e["id"] for e in b["Klei.AI.Effects"]["data"]["saveLoadEffects"]],
            "priorities": {k: v for k, v in prio.items() if v != 3},
        })
    return out


def biome_raster(s, W, H):
    """Rasterise WorldDetail overworld polygons onto the global grid (cell -> zone name index)."""
    gd = s.get("game_data") or {}
    cells = (gd.get("worldDetail") or {}).get("overworldCells") or []
    img = Image.new("I", (W, H), -1)
    d = ImageDraw.Draw(img)
    for c in cells:
        verts = (c.get("poly") or {}).get("vertices") or []
        if len(verts) >= 3:
            d.polygon([(vx, vy) for vx, vy in verts], fill=int(c["zoneType"]))
    return np.array(img, dtype=np.int32)


def _font(size):
    for f in ("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", "malgun.ttf", "AppleSDGothicNeo.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            from PIL import ImageFont
            return ImageFont.truetype(f, size)
        except Exception:
            pass
    from PIL import ImageFont
    return ImageFont.load_default()


SKIP_DOTS = {"Tile", "Ladder", "Wire", "LiquidConduit", "GasConduit", "SolidConduit", "LogicWire", "HighWattageWire",
             "InsulatedLiquidConduit", "LiquidConduitRadiant", "InsulatedGasConduit", "WireRefined"}


def render_map(path, E, M, B, wb, wd, ox, oy, title, cs=6):
    """1 cell = 1 tile grid. Thin line every tile, strong line every 10, coordinate ticks every 10
    (world-local, origin bottom-left), dimension lines with width x height in tiles."""
    sy, sx = E.shape
    ml, mt, mr, mb = 56, 70, 20, 56
    img = Image.new("RGB", (ml + sx * cs + mr, mt + sy * cs + mb), (255, 255, 255))
    d = ImageDraw.Draw(img)
    f, fb = _font(12), _font(15)
    X = lambda x: ml + x * cs
    Y = lambda y: mt + (sy - 1 - y) * cs  # top edge of cell row y
    for yy in range(sy):
        for xx in range(sx):
            d.rectangle([X(xx), Y(yy), X(xx) + cs - 1, Y(yy) + cs - 1], fill=color(E[yy, xx], M[yy, xx]))
    for b in wb:
        x, y = b["cell"][0] - ox, b["cell"][1] - oy
        if 0 <= x < sx and 0 <= y < sy and b["prefab"] not in SKIP_DOTS:
            d.rectangle([X(x) + 1, Y(y) + 1, X(x) + cs - 2, Y(y) + cs - 2], fill=(255, 255, 255))
    for m in wd:
        x, y = m["cell"][0] - ox, m["cell"][1] - oy
        if 0 <= x < sx and 0 <= y < sy:
            d.ellipse([X(x), Y(y), X(x) + cs, Y(y) + cs], fill=(255, 0, 0))
    # grid
    for xx in range(sx + 1):
        strong = xx % 10 == 0
        d.line([X(xx), mt, X(xx), mt + sy * cs], fill=(0, 0, 0) if strong else (60, 60, 60), width=1)
        if strong:
            d.line([X(xx), mt + sy * cs, X(xx), mt + sy * cs + 6], fill=(0, 0, 0))
            d.text((X(xx), mt + sy * cs + 8), str(xx), fill=(0, 0, 0), font=f, anchor="mt")
    for yy in range(sy + 1):
        strong = yy % 10 == 0
        py = mt + (sy - yy) * cs
        d.line([ml, py, ml + sx * cs, py], fill=(0, 0, 0) if strong else (60, 60, 60), width=1)
        if strong:
            d.line([ml - 6, py, ml, py], fill=(0, 0, 0))
            d.text((ml - 8, py), str(yy), fill=(0, 0, 0), font=f, anchor="rm")
    # biome borders (yellow) drawn on cell edges
    for yy in range(sy):
        for xx in range(sx):
            z = B[yy, xx]
            if xx + 1 < sx and B[yy, xx + 1] != z:
                d.line([X(xx + 1), Y(yy), X(xx + 1), Y(yy) + cs], fill=(255, 230, 0), width=2)
            if yy + 1 < sy and B[yy + 1, xx] != z:
                d.line([X(xx), Y(yy), X(xx) + cs, Y(yy)], fill=(255, 230, 0), width=2)
    # dimension lines
    yd = mt - 16
    d.line([X(0), yd, X(sx), yd], fill=(200, 0, 0), width=2)
    for xe in (X(0), X(sx)):
        d.line([xe, yd - 6, xe, yd + 6], fill=(200, 0, 0), width=2)
    d.text(((X(0) + X(sx)) // 2, yd - 4), f"가로 {sx} 타일", fill=(200, 0, 0), font=fb, anchor="mb")
    xd = ml + sx * cs + 10
    d.line([xd, mt, xd, mt + sy * cs], fill=(200, 0, 0), width=2)
    d.text((ml, 6), f"{title}  ·  세로 {sy} 타일  ·  1칸 = 1타일, 굵은 선 10타일, 좌표 원점 = 월드 왼쪽 아래 "
                    f"(전체 격자 기준 +{ox},+{oy})", fill=(0, 0, 0), font=f)
    d.text((ml, mt + sy * cs + 28), "분홍 = 심성석(Abyssalite) · 노란 선 = 바이옴 경계 · 흰 칸 = 건물 · 빨간 점 = 복제체",
           fill=(0, 0, 0), font=f)
    img.save(path)


def main(path, out):
    os.makedirs(out, exist_ok=True)
    s = onisave.load(path)
    worlds = world_list(s)
    sw, sh, cells, germ = read_sim(s["sim"])
    W, H = s["world"]["WidthInCells"], s["world"]["HeightInCells"]
    # sim grid has a 1-cell border: game cell (x, y) = sim (x+1, y+1); row 0 = bottom
    cells = cells[1:H + 1, 1:W + 1]
    germ = germ[1:H + 1, 1:W + 1]
    biome = biome_raster(s, W, H)

    uniq = np.unique(cells["e"])
    name_of = {int(h): ename(int(h)) for h in uniq}
    emap = np.vectorize(lambda h: name_of[int(h)], otypes=[object])(cells["e"])
    temp_c = cells["t"] - 273.15
    mass = cells["m"]

    dupes = duplicants(s, worlds)

    # buildings
    buildings = []
    for prefab, objs in s["groups"].items():
        for o in objs:
            if "_error" in o or not is_building(o):
                continue
            x, y = o["pos"][0], o["pos"][1]
            pe = prim(o)
            buildings.append({"prefab": prefab, "world": world_of(worlds, x, y), "cell": [int(math.floor(x)), int(math.floor(y))],
                              "material": ename(pe.get("ElementID", 0)) if pe else None,
                              "temp_c": round(pe["_Temperature"] - 273.15, 1) if pe else None})

    # resources: loose debris + storage contents
    res = collections.defaultdict(lambda: collections.Counter())
    food = collections.defaultdict(lambda: collections.Counter())
    for prefab, o, cont, x, y in walk_items(s):
        if is_building(o) or prefab in ("Minion",):
            continue
        b = o.get("behaviors", {})
        if "Pickupable" not in b and cont is None:
            continue
        pe = prim(o)
        if not pe:
            continue
        wid = world_of(worlds, x, y)
        units = pe.get("Units", 0) or 0
        if "Edible" in b or prefab in KCAL:
            food[wid][prefab] += units
        else:
            el = ename(pe.get("ElementID", 0))
            key = prefab if prefab not in ("", None) and ename(pe.get("ElementID", 0)) != prefab else el
            res[wid][key] += units

    # power
    power = collections.defaultdict(lambda: {"battery_kJ": 0.0, "batteries": 0, "generators": collections.Counter()})
    for prefab, objs in s["groups"].items():
        for o in objs:
            if "_error" in o or not is_building(o):
                continue
            wid = world_of(worlds, o["pos"][0], o["pos"][1])
            b = o["behaviors"]
            for bn in ("Battery", "BatterySmart"):
                d = (b.get(bn) or {}).get("data") or {}
                if "joulesAvailable" in d:
                    power[wid]["battery_kJ"] += d["joulesAvailable"] / 1000
                    power[wid]["batteries"] += 1
            if "EnergyGenerator" in b or prefab.endswith("Generator"):
                power[wid]["generators"][prefab] += 1

    gd = s.get("game_data") or {}
    settings = dict((gd.get("customGameSettings") or {}).get("CurrentQualityLevelsBySetting") or [])

    lines = []
    info = s["info"]
    lines.append(f"# {info['baseName']} 세이브 분석: 사이클 {info['numberOfCycles'] + 1}\n")
    lines.append(f"- 빌드 {s['build']}, 저장 버전 {info['saveMajorVersion']}.{info['saveMinorVersion']}, "
                 f"클러스터 `{info['clusterId']}`, 시드 {settings.get('WorldgenSeed')}")
    lines.append(f"- 난이도: " + ", ".join(f"{k} {v}" for k, v in settings.items()
                                          if k not in ("ClusterLayout", "WorldgenSeed", "SaveToCloud")))
    mods = [m["title"] for m in s["world"].get("active_mods") or []]
    lines.append(f"- 모드: {', '.join(mods) if mods else '없음'}\n")

    for w in worlds:
        wid = w["id"]
        wd = [d for d in dupes if d["world"] == wid]
        wb = [b for b in buildings if b["world"] == wid]
        if not wd and not w["visited"] and len(wb) < 5:
            continue
        ox, oy = w["offset"]
        sx, sy = w["size"]
        sl = (slice(oy, oy + sy), slice(ox, ox + sx))
        E, T, M, G, GC, B = emap[sl], temp_c[sl], mass[sl], germ["g"][sl], germ["c"][sl], biome[sl]
        lines.append(f"## 월드 {wid}: {w['worldName']} ({sx}×{sy}, 원점 {ox},{oy})"
                     + (" · 시작 행성" if w["start"] else ""))
        if w["storyTraits"]:
            lines.append(f"- 스토리 트레잇: {', '.join(w['storyTraits'])}")
        zc = collections.Counter(ZONE[z] if 0 <= z < len(ZONE) else str(z) for z in B.flatten() if z >= 0)
        lines.append("- 바이옴(셀 수): " + ", ".join(f"{k} {v}" for k, v in zc.most_common()))
        kat = int((E == "Katairite").sum())
        lines.append(f"- 심성석(Abyssalite) 셀: {kat}")
        lines.append(f"- 복제체 {len(wd)}명: " + ", ".join(d["name"] for d in wd))
        # base area = cells within 3 of any building
        mask = np.zeros(E.shape, bool)
        for b in wb:
            x, y = b["cell"][0] - ox, b["cell"][1] - oy
            mask[max(0, y - 3):y + 4, max(0, x - 3):x + 4] = True
        gasmask = mask & np.isin(E, list(GASES))
        if gasmask.any():
            gc = collections.Counter(E[gasmask])
            tot = gasmask.sum()
            lines.append("- 기지 주변 기체 셀 구성: " + ", ".join(
                f"{KO.get(k, k)} {v * 100 / tot:.0f}%" for k, v in gc.most_common(6)))
            o2 = gasmask & (E == "Oxygen")
            if o2.any():
                lines.append(f"- 산소 셀 평균 {M[o2].mean() * 1000:.0f} g, 중앙값 {np.median(M[o2]) * 1000:.0f} g "
                             f"(500 g 미만 {int((M[o2] < 0.5).sum())}셀)")
            lines.append(f"- 기지 주변 기체 온도: 평균 {T[gasmask].mean():.1f}°C, "
                         f"10~90% 구간 {np.percentile(T[gasmask], 10):.1f}~{np.percentile(T[gasmask], 90):.1f}°C, "
                         f"최고 {T[gasmask].max():.1f}°C")
        gm = mask & (G != 0)
        if gm.any():
            gg = collections.Counter()
            for h, c in zip(G[gm], GC[gm]):
                gg[GERMS.get(int(h), int(h))] += int(c)
            lines.append("- 기지 주변 세균: " + ", ".join(f"{k} {v:,}" for k, v in gg.most_common()))
        p = power.get(wid)
        if p:
            lines.append(f"- 전력: 배터리 {p['batteries']}개에 {p['battery_kJ']:.0f} kJ, 발전기 "
                         + ", ".join(f"{k} {v}" for k, v in p["generators"].items()))
        f = food.get(wid, {})
        if f:
            kc = sum(KCAL.get(k, 0) * v for k, v in f.items())
            unknown = [k for k in f if k not in KCAL]
            lines.append(f"- 식량: 약 {kc / 1000:,.0f} Mcal ({kc:,.0f} kcal) = "
                         + ", ".join(f"{k} {v:.0f}" for k, v in sorted(f.items(), key=lambda kv: -kv[1]))
                         + (f" (칼로리 미상: {', '.join(unknown)})" if unknown else ""))
            if wd:
                lines.append(f"  - 복제체 {len(wd)}명 × 1,000 kcal/사이클 기준 약 {kc / 1000 / len(wd):.1f} 사이클분")
        r = res.get(wid, {})
        if r:
            lines.append("- 자원(바닥+저장, kg 상위 20): " + ", ".join(
                f"{KO.get(k, k)} {v:,.0f}" for k, v in r.most_common(20)))
        bc = collections.Counter(b["prefab"] for b in wb)
        lines.append("- 건물 " + str(len(wb)) + "개: " + ", ".join(f"{k} {v}" for k, v in bc.most_common(40)))
        lines.append("")

        render_map(os.path.join(out, f"world_{wid}_map.png"), E, M, B, wb, wd, ox, oy,
                   f"World {wid} {w['worldName']}")
        np.savez_compressed(os.path.join(out, f"world_{wid}_grid.npz"),
                            element=E.astype(str), temp_c=T.astype(np.float32), mass_kg=M.astype(np.float32),
                            germ=np.vectorize(lambda h: GERMS.get(int(h), ""), otypes=[object])(G).astype(str),
                            germ_count=GC, biome=B, origin=np.array([ox, oy]))

    lines.append("## 복제체\n")
    lines.append("| 이름 | 월드 | 관심 | 주요 능력치(기본 레벨) | 스킬 | 남은 포인트(추정) | 스트레스 | 트레잇 |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for d in dupes:
        top = ", ".join(f"{k} {v}" for k, v in sorted(d["attributes"].items(), key=lambda kv: -kv[1])[:5])
        lines.append(f"| {d['name']} | {d['world']} | {', '.join(map(str, d['interests']))} | {top} | "
                     f"{', '.join(d['skills'])} | {d['unspent_points_est']} | {d['stress']} | {', '.join(d['traits'])} |")

    open(os.path.join(out, "report.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump({"info": info, "settings": settings, "worlds": worlds, "duplicants": dupes, "buildings": buildings,
               "resources": {str(k): dict(v) for k, v in res.items()},
               "food_units": {str(k): dict(v) for k, v in food.items()},
               "power": {str(k): {**v, "generators": dict(v["generators"])} for k, v in power.items()}},
              open(os.path.join(out, "colony.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
