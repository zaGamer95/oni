"""인게임 아이콘 받기: python3 _tools/blueprint/fetch_icons.py Pitcher_Pump Planter_Box ...

wiki.gg 원본(https://oxygennotincluded.wiki.gg/images/<Name>.png)을 받아 72px 정사각으로 줄여
assets/img/icons/<Name>.png 에 넣습니다. 재료·음식은 "Resource_Dirt:Dirt" 처럼. 이미 있으면 건너뜁니다. 페이지에서는 {% include i.html n="<Name>" %}.
"""
import io, os, sys, time, urllib.request
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'img', 'icons')
for a in sys.argv[1:]:
    # "Resource_Dirt:Dirt" = 위키 이름 Resource_Dirt 를 Dirt.png 로 저장 (재료·음식은 Resource_ 접두어)
    n, _, save = a.partition(':')
    dst = os.path.join(OUT, (save or n) + '.png')
    if os.path.exists(dst):
        continue
    url = 'https://oxygennotincluded.wiki.gg/images/' + n + '.png'
    for t in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (fan-guide icon fetch)'})
            data = urllib.request.urlopen(req, timeout=30).read()
            break
        except Exception as e:  # 429 등
            data = None
            err = e
            time.sleep(2 + 3 * t)
    if not data:
        print('FAIL', n, err)
        continue
    im = Image.open(io.BytesIO(data)).convert('RGBA')
    im.thumbnail((72, 72), Image.LANCZOS)
    c = Image.new('RGBA', (72, 72), (0, 0, 0, 0))
    c.paste(im, ((72 - im.width) // 2, (72 - im.height) // 2), im)
    c.save(dst, optimize=True)
    print('ok', n)
    time.sleep(1)
