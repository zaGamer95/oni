#!/usr/bin/env python3
"""Apply a wrong→official Korean name table (TSV) to the site's text files.
Row: wrong<TAB>official<TAB>english. With english set, only "wrong (english)" pairs are fixed;
without it, every occurrence is replaced. wrong may be a regex. Prints counts per row."""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP = ("/.git", "/_site", "/_sources", "/vendor", "/node_modules", "/assets", "/_tools/glossary")
rows = []
for line in open(sys.argv[1], encoding="utf-8"):
    if line.startswith("#") or not line.strip(): continue
    p = line.rstrip("\n").split("\t") + [""]
    rows.append((p[0], p[1], p[2].strip()))
files = []
for d, _, fs in os.walk(root):
    if any(s in d[len(root):] for s in SKIP): continue
    files += [os.path.join(d, f) for f in fs if f.endswith((".md", ".yml", ".html", ".py")) and f != "glossary_ko.yml"]
texts = {f: open(f, encoding="utf-8").read() for f in files}
tot = 0
for wrong, right, en in rows:
    if en:
        rx = re.compile(r"(?<![가-힣])" + wrong + r"(\**\s?\(\s?" + re.escape(en) + r"\s?\))")
        rep = lambda m: right + m.group(1)
    else:
        rx = re.compile(r"(?<![가-힣])" + wrong if not wrong.startswith("(?") else wrong)
        rep = lambda m: right
    n = 0
    for f in files:
        new, k = rx.subn(rep, texts[f])
        if k: texts[f] = new; n += k
    tot += n
    print(f"{n:3d}  {wrong} -> {right}" + (f"  ({en})" if en else ""))
for f in files:
    if texts[f] != open(f, encoding="utf-8").read():
        open(f, "w", encoding="utf-8").write(texts[f])
print("total", tot)
