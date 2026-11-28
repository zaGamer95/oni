"""지원 건물 (Support Buildings, U60-763796) 배치 도면 3장.

범위는 위키 Cell of Interest 값 (건물 왼쪽 아래 칸 기준):
- 연구 도구 (Study Tools) 1×4: 좌우 2칸, 아래 2줄. +5% 연구 속도, 겹침 (최대 4개)
- 조리 도구 (Cooking Tools) 3×1: 좌우 2칸, 자기 줄 + 아래 2줄. +15%, 안 겹침
- 워크숍 도구 (Workshop Tools) 3×1: 좌우 4칸, 자기 줄 + 아래 2줄. +15%, 안 겹침, 뒷벽 필요
- 단조 도구 (Forge Tools) 1×2: 좌우 4칸, 자기 2줄. +15%, 안 겹침
호환 건물 칸이 범위에 한 칸이라도 들어가면 보너스.
"""
from bp import BP, C

RANGE = '#00dcb4'


def _shell(d, w, h=4):
    """벽 안쪽 w×h 방. 벽 줄 y=0 / y=h+1, 벽 칸 x=0 / x=w+1."""
    d.tiles(0, 0, w + 2, 1)
    d.tiles(0, h + 1, w + 2, 1)
    d.tiles(0, 1, 1, h)
    d.tiles(w + 1, 1, 1, h)
    d.door(0, h - 1)
    d.door(w + 1, h - 1)


def _range(d, x, y, w, h):
    d.fill(x, y, w, h, RANGE, op=.16, dash=True, stroke=RANGE, layer='over')


def lab():
    W, H = 24, 4
    d = BP('support-lab', cols=W + 2, rows=H + 2, unit=30, x0=1, y0=1,
           title='포드층 연구실 24×4 + 연구 도구 (Study Tools) 8개', legend_cols=1,
           note='배치도의 연구소(3~4번)·포드(11~14번)·슈퍼컴퓨터(18~20번)는 그대로 두고, 각 연구 건물 양옆 2칸씩 책장 1×4를 세웁니다.\n'
                '책장 범위 = 좌우 2칸 · 아래 2줄 (청록 점선). 연구 건물 한 칸이라도 걸리면 +5%, 최대 4개 겹쳐서 +20%.')
    _shell(d, W, H)
    d.room(1, 1, W, H, None, 'research', dims='wh')
    y = H + 1
    d.bld(11, y - 4, 4, 4, 'Printing_Pod', '포드 4×4', title='프린팅팟 4×4')
    d.bld(3, y - 2, 2, 2, 'Research_Station', None, color='#e0a0ff', title='연구스테이션 (Research Station) 2×2')
    d.bld(18, y - 3, 3, 3, 'Super_Computer', None, color='#e0a0ff', title='슈퍼컴퓨터 (Super Computer) 3×3')
    for x in (1, 2, 5, 6, 16, 17, 21, 22):
        d.bld(x, y - 4, 1, 4, 'Study_Tools', None, color='#9fe8d8', title='연구 도구 (Study Tools) 1×4')
    # 범위 예시 2개 (연구소 왼쪽 첫 책장, 슈퍼컴 오른쪽 끝 책장)
    _range(d, 2 - 2, y - 2, 5, 2)
    _range(d, 22 - 2, y - 2, 5, 2)
    d.text(3.5 + .5, 1.2, '연구소 +20%', '#e0a0ff', 10, bold=True, halo=True)
    d.text(19.5, 1.2, '슈퍼컴 +20%', '#e0a0ff', 10, bold=True, halo=True)
    d.key('icon', '연구 도구 (Study Tools) 1×4 · 원석 400 kg + 섬유 2 · 연구 High Culture', 'Study_Tools')
    d.key('icon', '연구소 2×2 · 슈퍼컴퓨터 3×3 (호환)', 'Research_Station')
    d.key('fill', '책장 1개의 효과 범위 (예시 2개만 표시)', RANGE)
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def kitchen():
    W, H = 24, 4
    d = BP('support-kitchen', cols=W + 2, rows=H + 2, unit=30, x0=1, y0=1,
           title='주방 24×4 + 조리 도구 (Cooking Tools) 1개', legend_cols=1,
           note='조리 도구는 냄비 걸이 모양(3×1)입니다. 천장 바로 아래 1번 줄, 3~5번 칸에 걸면 자기 줄 + 아래 2줄이 범위라,\n'
                '향신료 분쇄기 · 전기 그릴 · 가스 레인지 세 대가 한 번에 +15%. 겹치지 않으니 한 조리대 묶음에 1개면 충분.')
    _shell(d, W, H)
    d.room(1, 1, W, H, None, 'food', dims='wh')
    y = H + 1
    d.bld(1, y - 3, 2, 3, 'Spice_Grinder', None, color='#ffe284', title='향신료 분쇄기 (Spice Grinder) 2×3')
    d.bld(3, y - 2, 3, 2, 'Electric_Grill', None, color='#ffb070', title='전기 그릴 (Electric Grill) 3×2')
    d.bld(6, y - 3, 3, 3, 'Gas_Range', None, color='#ffb070', planned=True,
          title='가스 레인지 (Gas Range) 3×3, Enhanced Seasoning 스킬 필요')
    d.bld(3, 1, 3, 1, 'Cooking_Tools', None, color='#9fe8d8', title='조리 도구 (Cooking Tools) 3×1')
    for x in range(11, 15):
        d.bld(x, y - 2, 1, 2, 'Refrigerator', None, color='#6aa8ff', title='냉장고 1×2')
    _range(d, 1, 1, 7, 3)
    d.key('icon', '조리 도구 (Cooking Tools) 3×1 · 정제 금속 200 kg · 연구 Home Luxuries', 'Cooking_Tools')
    d.key('icon', '향신료 분쇄기 · 전기 그릴 · 가스 레인지(점선 = 나중)', 'Electric_Grill')
    d.key('icon', '냉장고 (범위 밖이어도 됨)', 'Refrigerator')
    d.key('fill', '조리 도구 효과 범위 7×3', RANGE)
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def refining():
    W, H = 14, 4
    d = BP('support-refining', cols=W + 2, rows=H + 2, unit=34, x0=1, y0=1,
           title='정제·제련 14×4 + 워크숍 도구 (Workshop Tools) · 단조 도구 (Forge Tools)', legend_cols=1,
           note='워크숍 도구(선반, 뒷벽 필요)는 6~8번 맨 윗줄 → 범위 좌우 4칸 · 아래 2줄 = 쇄석기 + 제작 스테이션.\n'
                '단조 도구 1×2는 8번 바닥 → 범위 좌우 4칸 · 자기 2줄 = 금속 제련소 + 가마. 금속 제련소는 배치도보다 2칸 오른쪽(9~11번).')
    _shell(d, W, H)
    d.room(1, 1, W, H, None, 'ind', dims='wh')
    y = H + 1
    d.bld(2, y - 4, 4, 4, 'Rock_Crusher', None, title='쇄석기 (Rock Crusher) 4×4')
    d.bld(6, 1, 3, 1, 'Workshop_Tools', None, color='#9fe8d8', title='워크숍 도구 (Workshop Tools) 3×1, 뒷벽')
    d.bld(6, y - 2, 2, 2, 'Crafting_Station', None, color='#c0c8e0', title='제작 스테이션 (Crafting Station) 2×2')
    d.bld(8, y - 2, 1, 2, 'Forge_Tools', None, color='#9fe8d8', title='단조 도구 (Forge Tools) 1×2')
    d.bld(9, y - 4, 3, 4, 'Metal_Refinery', None, color='#ff9a7a', planned=True,
          title='금속 제련소 (Metal Refinery) 3×4, 냉방실 생긴 뒤')
    d.bld(12, y - 2, 2, 2, 'Kiln', None, color='#ff9a7a', title='가마 (Kiln) 2×2')
    _range(d, 6 - 4, 1, 11, 3)
    _range(d, 8 - 4, y - 2, 9, 2)
    d.key('icon', '워크숍 도구 3×1 · 금속 광석 400 kg + 목재 100 kg · 연구 Plastic Manufacturing', 'Workshop_Tools')
    d.key('icon', '단조 도구 1×2 · 세라믹 600 kg + 정제 금속 200 kg · 연구 Solid Control', 'Forge_Tools')
    d.key('icon', '쇄석기 · 제작 스테이션 (워크숍 도구 호환)', 'Rock_Crusher')
    d.key('icon', '금속 제련소(점선 = 나중) · 가마 (단조 도구 호환)', 'Metal_Refinery')
    d.key('fill', '효과 범위 (위: 워크숍 도구 11×3, 아래: 단조 도구 9×2)', RANGE)
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def build():
    return [lab(), kitchen(), refining()]
