#!/usr/bin/env python3
"""After a name swap, fix Korean particles (을/를, 은/는, 이/가, 과/와, 으로/로, 이에요/예요)
that follow the given official names. Usage: fix_particles.py <fixes.tsv>"""
import os, re, sys
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP = ("/.git", "/_site", "/_sources", "/vendor", "/node_modules", "/assets", "/_tools/glossary")
names = set()
for line in open(sys.argv[1], encoding="utf-8"):
    if line.startswith("#") or not line.strip(): continue
    names.add(line.split("\t")[1].strip())
def jong(ch):
    c = ord(ch) - 0xAC00
    return None if not 0 <= c < 11172 else c % 28   # 0 = no final consonant, 8 = ㄹ
PAIRS = [("을", "를"), ("은", "는"), ("이", "가"), ("과", "와")]
def fix(name, part):
    j = jong(name[-1])
    if j is None: return part
    has = j != 0
    for a, b in PAIRS:
        if part in (a, b): return a if has else b
    if part in ("으로", "로"): return "으로" if has and j != 8 else "로"
    if part in ("이에요", "예요"): return "이에요" if has else "예요"
    return part
files = []
for d, _, fs in os.walk(root):
    if any(s in d[len(root):] for s in SKIP): continue
    files += [os.path.join(d, f) for f in fs if f.endswith((".md", ".yml", ".html", ".py")) and f != "glossary_ko.yml"]
alt = "|".join(sorted(map(re.escape, names), key=len, reverse=True))
rx = re.compile(r"(" + alt + r")(\**(?:\s?\([A-Za-z0-9'\-\.: ]+\))?\**)(이에요|예요|으로|을|를|은|는|이|가|과|와|로)(?![가-힣])")
total = 0
for f in files:
    t = open(f, encoding="utf-8").read()
    n = [0]
    def rep(m):
        p = fix(m.group(1), m.group(3))
        if p != m.group(3): n[0] += 1
        return m.group(1) + m.group(2) + p
    new = rx.sub(rep, t)
    if n[0]:
        open(f, "w", encoding="utf-8").write(new); total += n[0]
        print(n[0], f[len(root)+1:])
print("particles fixed", total)
