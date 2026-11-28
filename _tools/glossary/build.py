#!/usr/bin/env python3
"""Build _data/glossary_ko.yml from the game's official Korean strings file.

Usage:
  python3 _tools/glossary/build.py <strings_preinstalled_ko_klei.po> [build]

The .po ships with the game:
  macOS  ~/Library/Application Support/Steam/steamapps/common/OxygenNotIncluded/
         OxygenNotIncluded.app/Contents/Resources/Data/StreamingAssets/strings/
  Win    <Steam>/steamapps/common/OxygenNotIncluded/OxygenNotIncluded_Data/StreamingAssets/strings/
Only proper names (msgctxt ending in .NAME in the categories below) are kept.
"""
import json, re, sys, os
from collections import OrderedDict

# (category label, msgctxt regex). Order = priority when one English name has several entries.
CATS = [
    ("critter",   r"^STRINGS\.CREATURES\.SPECIES\.(?!GEYSER\.|SEEDS\.)[A-Z0-9_]+(\.(BABY|VARIANT_[A-Z0-9_]+(\.BABY)?))?\.NAME$"),
    ("seed",      r"^STRINGS\.CREATURES\.SPECIES\.SEEDS\.[A-Z0-9_]+\.NAME$"),
    ("geyser",    r"^STRINGS\.CREATURES\.SPECIES\.GEYSER\.[A-Z0-9_]+\.NAME$"),
    ("building",  r"^STRINGS\.BUILDINGS\.PREFABS\.[A-Z0-9_]+\.NAME$"),
    ("element",   r"^STRINGS\.ELEMENTS\.[A-Z0-9_]+\.NAME$"),
    ("item",      r"^STRINGS\.ITEMS\.[A-Z0-9_]+\.[A-Z0-9_]+\.NAME$"),
    ("equipment", r"^STRINGS\.EQUIPMENT\.PREFABS\.[A-Z0-9_]+\.NAME$"),
    ("skill",     r"^STRINGS\.DUPLICANTS\.ROLES\.[A-Z0-9_]+\.NAME$"),
    ("skill_group", r"^STRINGS\.DUPLICANTS\.SKILLGROUPS\.[A-Z0-9_]+\.NAME$"),
    ("chore_group", r"^STRINGS\.DUPLICANTS\.CHOREGROUPS\.[A-Z0-9_]+\.NAME$"),
    ("attribute", r"^STRINGS\.DUPLICANTS\.ATTRIBUTES\.[A-Z0-9_]+\.NAME$"),
    ("trait",     r"^STRINGS\.DUPLICANTS\.TRAITS\.[A-Z0-9_]+\.NAME$"),
    ("disease",   r"^STRINGS\.DUPLICANTS\.DISEASES\.[A-Z0-9_]+\.NAME$"),
    ("research",  r"^STRINGS\.RESEARCH\.TECHS\.[A-Z0-9_]+\.NAME$"),
    ("room",      r"^STRINGS\.ROOMS\.TYPES\.[A-Z0-9_]+\.NAME$"),
    ("world_trait", r"^STRINGS\.WORLD_TRAITS\.[A-Z0-9_]+\.NAME$"),
    ("subworld",  r"^STRINGS\.SUBWORLDS\.[A-Z0-9_]+\.NAME$"),
    ("world",     r"^STRINGS\.WORLDS\.[A-Z0-9_]+\.NAME$"),
    ("cluster",   r"^STRINGS\.CLUSTER_NAMES\.[A-Z0-9_]+\.NAME$"),
    ("robot",     r"^STRINGS\.ROBOTS\.MODELS\.[A-Z0-9_]+\.NAME$"),
    ("story_trait", r"^STRINGS\.CODEX\.STORY_TRAITS\.[A-Z0-9_]+\.NAME$"),
]
CATS = [(c, re.compile(r)) for c, r in CATS]

def unq(s): return json.loads(s)

def parse(path):
    ents, cur, key = [], {}, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            if cur: ents.append(cur)
            cur, key = {}, None
            continue
        if line.startswith("#"): continue
        m = re.match(r'(msgctxt|msgid|msgstr)\s+(".*")$', line)
        if m: key = m.group(1); cur[key] = unq(m.group(2)); continue
        if line.startswith('"') and key: cur[key] += unq(line)
    if cur: ents.append(cur)
    return [e for e in ents if e.get("msgctxt")]

def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()

def yq(s): return json.dumps(s, ensure_ascii=False)

def main():
    po = sys.argv[1]
    build = sys.argv[2] if len(sys.argv) > 2 else (re.findall(r"_(\d{6})", open(po, encoding="utf-8").read(400)) or ["?"])[0]
    out = OrderedDict()   # english -> dict
    for e in parse(po):
        ctx = e["msgctxt"]
        cat = next((c for c, r in CATS if r.match(ctx)), None)
        if not cat: continue
        en, ko = clean(e.get("msgid", "")), clean(e.get("msgstr", ""))
        if not en or not ko or "{" in en: continue
        if en in out:
            if ko != out[en]["ko"] and ko not in out[en].get("also", []):
                out[en].setdefault("also", []).append(ko)
            continue
        out[en] = {"ko": ko, "cat": cat, "key": ctx.replace("STRINGS.", "")}
    order = {c: i for i, (c, _) in enumerate(CATS)}
    items = sorted(out.items(), key=lambda kv: (order[kv[1]["cat"]], kv[0].lower()))
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dst = os.path.join(root, "_data", "glossary_ko.yml")
    with open(dst, "w", encoding="utf-8") as f:
        f.write("# 공식 한국어 용어집 (Oxygen Not Included, Klei 공식 한국어 번역)\n")
        f.write(f"# 출처: 게임 내장 strings_preinstalled_ko_klei.po (빌드 {build}). 생성: _tools/glossary/build.py\n")
        f.write("# 손으로 고치지 말 것. 이름은 이 파일의 ko 값만 쓴다. 키 = 영어 이름(게임 영문 UI).\n")
        f.write("# also = 같은 영어 이름이 다른 곳에서 다르게 번역된 경우 (게임 원문 그대로).\n")
        f.write(f"_source: {{file: strings_preinstalled_ko_klei.po, build: {yq(build)}, terms: {len(items)}}}\n")
        for en, d in items:
            extra = f", also: [{', '.join(yq(a) for a in d['also'])}]" if d.get("also") else ""
            f.write(f"{yq(en)}: {{ko: {yq(d['ko'])}, cat: {d['cat']}, key: {d['key']}{extra}}}\n")
    from collections import Counter
    print(dst, len(items), dict(Counter(d["cat"] for _, d in items)))

if __name__ == "__main__":
    main()
