"""도면 빌드: python3 _tools/blueprint/make.py [--preview DIR] [--icons RAW_DIR]

- specs/*.py 의 build() 가 돌려주는 BP 들을 _includes/bp/<이름>.svg 로 씁니다.
- --icons RAW_DIR: 위키에서 받은 원본 아이콘(<Name>.png)을 64px로 줄여 assets/img/icons/ 에 넣습니다.
  (원본: https://oxygennotincluded.wiki.gg/images/<Name>.png)
- --preview DIR: 아이콘을 로컬 경로로 쓴 미리보기 SVG/HTML 을 DIR 에 씁니다.
"""
import importlib.util, glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from bp import ICON_DIR  # noqa

args = sys.argv[1:]
preview = args[args.index('--preview') + 1] if '--preview' in args else None
raw = args[args.index('--icons') + 1] if '--icons' in args else None
only = [a for a in args if not a.startswith('--') and a not in (preview, raw)]

out_dir = os.path.join(ROOT, '_includes', 'bp')
os.makedirs(out_dir, exist_ok=True)
os.makedirs(ICON_DIR, exist_ok=True)

used = set()
pages = []
for f in sorted(glob.glob(os.path.join(HERE, 'specs', '*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for d in m.build():
        if only and d.name not in only:
            continue
        s, W = d.svg('{{ site.baseurl }}/assets/img/icons/')
        open(os.path.join(out_dir, d.name + '.svg'), 'w').write(s + '\n')
        used |= d.icons
        if preview:
            os.makedirs(preview, exist_ok=True)
            p, _ = d.svg('file://' + os.path.abspath(ICON_DIR) + '/')
            open(os.path.join(preview, d.name + '.svg'), 'w').write(p)
            pages.append(d.name)
        print('wrote', d.name, int(W), 'px')

if raw:
    from PIL import Image
    for n in sorted(used):
        src = os.path.join(raw, n + '.png')
        dst = os.path.join(ICON_DIR, n + '.png')
        if not os.path.exists(src):
            print('MISSING icon', n)
            continue
        im = Image.open(src).convert('RGBA')
        im.thumbnail((72, 72), Image.LANCZOS)
        im.save(dst, optimize=True)
missing = [n for n in used if not os.path.exists(os.path.join(ICON_DIR, n + '.png'))]
if missing:
    print('아이콘 없음:', missing)
