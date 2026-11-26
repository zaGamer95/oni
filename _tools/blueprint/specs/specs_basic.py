from bp import BP, C


def floors():
    d = BP('build-floors', cols=40, rows=26, unit=16, x0=1, y0=1, title='기지 층 배치 예시 (층 = 내부 4칸 + 바닥 1칸)',
           legend_cols=2,
           note='가운데 세로 통로(사다리 + 소방봉)를 기준으로 같은 층을 반복해 쌓습니다. 방 하나 16×4 = 64칸 → 대부분 방의 최대 크기.\n'
                '발전 구역은 생활층 아래에 두되 단열 타일로 따로 감싸고, 무거운 CO₂는 맨 아래 구덩이에 모입니다.')
    o = 1
    rooms = [('침실', 'bed', '연구 · 작업장', 'research'), ('식당 · 주방', 'food', '농장', 'farm'),
             ('화장실 · 세면기', 'wash', '보관함', 'misc')]
    for i, (a, ka, b, kb) in enumerate(rooms):
        y = o + 1 + i * 5
        d.room(o + 1, y, 16, 4, a, ka, dims='wh' if i == 0 else 'h', label_at='mid', size_in_label=(i == 0))
        d.room(o + 21, y, 16, 4, b, kb, dims='' if i else 'w', label_at='mid', size_in_label=False)
        d.door(o + 17, y + 2)
        d.door(o + 20, y + 2)
    d.fill(o + 18, o, 2, 16, '#2a2618', open=True)
    d.ladder(o + 18, o, 16)
    d.pole(o + 19, o, 16)
    d.autowalls(o, o, 38, 16, 'tile')
    d.tiles(o, o + 15, 38, 1, 'ins')
    d.room(o + 1, o + 16, 36, 4, '발전기 · 전기분해기 (뜨거움, 단열 타일로 감싸기)', 'ind', dims='h', label_at='mid', size_in_label=False)
    d.tiles(o, o + 16, 1, 4, 'ins'); d.tiles(o + 37, o + 16, 1, 4, 'ins'); d.tiles(o, o + 20, 38, 1, 'ins')
    d.room(o + 1, o + 21, 36, 3, 'CO₂ 구덩이 (무거운 이산화탄소가 모이는 곳)', 'plan', dims='h', label_at='mid', size_in_label=False)
    d.fill(o + 1, o + 22, 36, 2, C['co2'], op=.35)
    d.tiles(o, o + 21, 1, 4); d.tiles(o + 37, o + 21, 1, 4); d.tiles(o, o + 24, 38, 1)
    d.dim(o + 18, o + 20, o - .5, '통로 2')
    d.key('icon', '사다리 (올라갈 때)', 'Ladder')
    d.key('icon', '소방봉 (내려갈 때 훨씬 빠름)', 'Fire_Pole')
    d.key('tile', '단열 타일 (발전 구역 감싸기)', 'ins')
    d.key('fill', 'CO₂ (무거워서 아래로)', C['co2'])
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def bath_flow():
    d = BP('bath-flow', cols=22, rows=7, unit=26, x0=1, y0=1, title='화장실 동선: 변소 16×3, 화장실 → 세면기 → 문 (바닥 18칸)',
           legend_cols=1,
           note='나가는 길이 세면기를 통과하게. 간이 화장실 2×3 ×4 + 세면기 2×3 ×4 = 16칸 + 문 1칸 + 벽 1칸 = 바닥 18칸.')
    o = 1
    d.tiles(o, o, 19, 1); d.tiles(o, o + 4, 19, 1); d.tiles(o, o + 1, 1, 3); d.tiles(o + 17, o + 1, 1, 1)
    d.room(o + 1, o + 1, 16, 3, None, 'wash', dims='wh')
    for i in range(4):
        d.bld(o + 1 + 2 * i, o + 1, 2, 3, 'Outhouse', None, color='#c8a070', title='간이 화장실 2×3')
        d.bld(o + 9 + 2 * i, o + 1, 2, 3, 'Wash_Basin', '→', color='#9fe8ff', title='세면기 2×3 (나가는 방향으로)')
    d.door(o + 17, o + 2)
    d.dim(o, o + 18, o + 4.5 + 1, '바닥 18')
    d.text(o + 18.2, o + 3.3, '기지 쪽 →', '#acffbd', 11, anchor='start', bold=True)
    d.key('icon', '간이 화장실 2×3 (나중에 수세식 화장실)', 'Outhouse')
    d.key('icon', '세면기 2×3, 화살표 = 손 씻는 방향 (나가는 쪽)', 'Wash_Basin')
    d.key('icon', '문', 'Pneumatic_Door')
    return d


def build():
    return [floors(), bath_flow()]
