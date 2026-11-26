from bp import BP, C


def _mess_shell(d, oy, kitchen):
    T = lambda x, y, w, h, k='tile': d.tiles(x, oy + y, w, h, k)
    T(0, 0, 3, 2); T(0, 6, 3, 1)
    d.room(0, oy + 2, 3, 4, None, 'misc', dims='')
    d.text(1.5, oy + 1.6, kitchen, C['dim'], 9.5, halo=True)
    T(3, 0, 1, 7); T(7, 0, 1, 7); T(32, 0, 1, 7)
    T(8, 0, 24, 1); T(8, 6, 24, 1)
    d.fill(4, oy, 3, 7, '#24452e')
    d.ladder(5, oy, 7)
    d.pole(6, oy, 7)
    d.fill(33, oy, 2, 7, '#2a2618')
    d.ladder(33, oy, 7)
    d.pole(34, oy, 7)
    for x in (3, 7, 32):
        d.door(x, oy + 4)


def mess_early():
    oy = 1
    d = BP('mess-early', cols=35, rows=8, unit=18, x0=8, y0=oy,
           title='초반: 24×5 자리를 다 파고, 13번에 임시 벽 → 왼쪽 12×5 = 60칸만 식당', legend_cols=2,
           note='식당(Mess Hall)은 최대 64칸이라 120칸 그대로면 식당 보너스(+3)가 없음 → 임시 벽으로 60칸.\n'
                '식탁 4·6·8·10번 · 쿨러·꽃병은 오른쪽(18~21번)에 연구되면 (점선) · 분쇄기·배급 상자는 서쪽 보관·조리 칸.')
    _mess_shell(d, oy, '← 보관·조리')
    d.room(8, oy + 1, 12, 5, '식당', 'food', dims='wh', label_at='top')
    d.tiles(20, oy + 1, 1, 5)
    d.fill(20, oy + 1, 1, 5, 'none', stroke='#ffe284', dash=True, layer='over')
    d.room(21, oy + 1, 11, 5, '나중에 큰 회관', 'plan', dims='w', dashed=True, label_at='top', size_in_label=False)
    d.dim(8, 32, oy + 6.5, '파 둘 칸 24')
    for x in (11, 13, 15, 17):
        d.bld(x, oy + 5, 1, 1, 'Mess_Table', None, color='#ffe284', title='식탁 1×1')
    d.bld(25, oy + 4, 2, 2, 'Water_Cooler', None, color='#6aa8ff', planned=True, title='워터 쿨러 2×2 (연구 후)')
    d.bld(28, oy + 4, 1, 2, 'Flower_Pot', None, color='#ff9fd0', planned=True, title='꽃병 (연구 후)')
    d.key('icon', '식탁 1×1', 'Mess_Table')
    d.key('fill', '13번 = 임시 벽 (나중에 허묾)', '#ffe284')
    d.key('icon', '워터 쿨러 2×2 (꺼 둠) · 꽃병: 연구되면', 'Water_Cooler')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def mess_late():
    oy = 1
    d = BP('mess-late', cols=35, rows=8, unit=18, x0=8, y0=oy,
           title='후반: 복층 큰 회관 24×5 (가운데 3번째 줄에 발판)', legend_cols=2,
           note='아래층 식탁 8 (5~19번 홀수) · 위층 식탁 6 (6~16번 짝수) + 워터 쿨러(꺼 둠, 18~19번) · 꽃병(블러프 브라이어) 2번.\n'
                '발판 = 4~21번 칸 3번째 줄 타일 18개, 양 끝 3·22번에 방 안 사다리 · 방 크기 120 − 발판 18 = 102칸 (큰 회관 32~120).')
    _mess_shell(d, oy, '← 주방 24')
    d.room(8, oy + 1, 24, 5, '복층 큰 회관', 'food', dims='wh', label_at='top')
    d.tiles(11, oy + 3, 18, 1)
    d.dim(11, 29, oy + 6.5, '발판 18')
    d.ladder(10, oy + 1, 5)
    d.ladder(29, oy + 1, 5)
    for x in range(12, 27, 2):
        d.bld(x, oy + 5, 1, 1, 'Mess_Table', None, color='#ffe284', title='식탁 (아래층)')
    for x in range(13, 24, 2):
        d.bld(x, oy + 2, 1, 1, 'Mess_Table', None, color='#ffe284', title='식탁 (위층)')
    d.bld(25, oy + 1, 2, 2, 'Water_Cooler', None, color='#6aa8ff', title='워터 쿨러 2×2 (꺼 둠)')
    d.bld(9, oy + 4, 1, 2, 'Flower_Pot', None, color='#ff9fd0', title='꽃병 (블러프 브라이어)')
    d.key('icon', '식탁 1×1 (위 6 + 아래 8 = 14)', 'Mess_Table')
    d.key('tile', '발판 = 일반 타일 18개', 'tile')
    d.key('icon', '방 안 사다리 (3·22번)', 'Ladder')
    d.key('icon', '워터 쿨러 2×2 (오락 건물, 꺼 둠)', 'Water_Cooler')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def _gh_shell(d, ox, oy):
    T = lambda x, y, w, h, k='tile': d.tiles(ox + x, oy + y, w, h, k)
    T(1, 0, 25, 1); T(1, 1, 1, 5); T(1, 6, 1, 1); T(22, 6, 3, 1); T(25, 1, 1, 5)
    T(9, 7, 1, 7); T(9, 14, 1, 1); T(22, 14, 4, 1); T(25, 7, 1, 7)
    d.fill(ox + 26, oy, 2, 15, '#2a2618')
    d.ladder(ox + 26, oy, 15)
    d.pole(ox + 27, oy, 15)
    d.door(ox + 25, oy + 4)
    d.door(ox + 25, oy + 12)


def greenhouse_early():
    ox, oy = 0, 1
    d = BP('greenhouse-early', cols=29, rows=17, unit=16, x0=ox + 2, y0=oy + 1,
           title='초반: 바닥 농장 타일 한 줄', legend_cols=1,
           note='바닥 농장 타일 20 = 끼니나무 20 = 4,000 kcal (4명). 통로 쪽 끝 3칸 중 맨 끝 1칸에 사다리.')
    _gh_shell(d, ox, oy)
    d.room(ox + 2, oy + 1, 23, 5, '온실 A', 'farm', dims='wh', label_at='top')
    d.tiles(ox + 2, oy + 6, 20, 1, 'farm')
    d.plants(ox + 2, oy + 5, 20, 'Mealwood', title='끼니나무')
    d.ladder(ox + 24, oy + 1, 5)
    d.room(ox + 10, oy + 7, 15, 7, '온실 B 자리', 'plan', dims='wh', dashed=True, label_at='top', dim_w_at=oy + 14.5)
    d.key('tile', '농장 타일 (바닥 줄 20칸)', 'farm')
    d.key('icon', '끼니나무 1×2 (20그루)', 'Mealwood')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def greenhouse_late():
    ox, oy = 0, 1
    d = BP('greenhouse-late', cols=29, rows=17, unit=16, x0=ox + 2, y0=oy + 1,
           title='후반: 2줄 온실 A + 조명 온실 B', legend_cols=1,
           note='A: 끼니나무 40, 작업대 없음 (끼니나무는 농부의 손길을 못 받음) · B: 센털꽃 24 + 천장 조명 4 + 농업 작업대.\n'
                'B 줄 (위에서): 1 조명 · 2~3 센털꽃 · 4 농장 타일 · 5 조명(타일 아래) · 6~7 센털꽃 · 바닥 농장 타일.')
    _gh_shell(d, ox, oy)
    d.room(ox + 2, oy + 1, 23, 5, '온실 A', 'farm', dims='wh', label_at='top')
    d.tiles(ox + 2, oy + 3, 20, 1, 'farm')
    d.tiles(ox + 22, oy + 3, 2, 1)
    d.tiles(ox + 2, oy + 6, 20, 1, 'farm')
    d.plants(ox + 2, oy + 2, 20, 'Mealwood', title='끼니나무')
    d.plants(ox + 2, oy + 5, 20, 'Mealwood', title='끼니나무')
    d.ladder(ox + 24, oy + 1, 5)
    d.room(ox + 10, oy + 7, 15, 7, '온실 B (센털꽃)', 'farm', dims='wh', label_at='top', dim_w_at=oy + 14.5)
    d.tiles(ox + 10, oy + 10, 12, 1, 'farm')
    d.tiles(ox + 22, oy + 10, 2, 1)
    d.tiles(ox + 10, oy + 14, 12, 1, 'farm')
    d.plants(ox + 10, oy + 9, 12, 'Bristle_Blossom', title='센털꽃')
    d.plants(ox + 10, oy + 13, 12, 'Bristle_Blossom', title='센털꽃')
    for x in (12, 19):
        for y in (7, 11):
            d.bld(ox + x, oy + y, 1, 1, 'Ceiling_Light', None, color='#fff6a0', title='천장 조명')
    d.bld(ox + 22, oy + 11, 2, 3, 'Farm_Station', '작업대', color='#cdf248', title='농업 작업대 2×3')
    d.ladder(ox + 24, oy + 7, 7)
    d.key('tile', '농장 타일', 'farm')
    d.key('icon', '끼니나무 (A, 40그루)', 'Mealwood')
    d.key('icon', '센털꽃 (B, 24그루, 빛 200 lux 이상)', 'Bristle_Blossom')
    d.key('icon', '천장 조명 1×1', 'Ceiling_Light')
    d.key('icon', '농업 작업대 2×3', 'Farm_Station')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def build():
    return [mess_early(), mess_late(), greenhouse_early(), greenhouse_late()]
