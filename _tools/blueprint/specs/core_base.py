from bp import BP, C

OX, OY = 2, 2  # 여백 (치수선·격벽 자리)


def walls(d, cols, rows):
    """방이 아닌 칸 중 기지 안쪽 줄(층 바닥·벽)을 타일로 깔 영역."""


def late():
    d = BP('core-base-late', cols=104, rows=52, unit=11, x0=OX, y0=OY, label_every=5,
           title='후반 완성 배치도 (1칸 = 1타일)', legend_cols=3,
           note='방 안 아이콘 = 실제 건물 크기 (편안한 침대 4×2, 수세식 화장실·싱크대 2×3, 샤워기 2×4, 포드 4×4, 석탄 발전기 3×3 …).\n'
                '왼쪽이 서쪽, 오른쪽이 동쪽. 방마다 위 벽 줄에 가로, 왼쪽 벽 줄에 세로 칸 수(벽 제외).')

    def R(x, y, w, h, name, kind, sub=None, dims='wh', **kw):
        d.room(OX + x, OY + y, w, h, name, kind, sub=sub, dims=dims, **kw)

    def B(x, y, w, h, icon, title=None, color='#c0c8e0', **kw):
        d.bld(OX + x, OY + y, w, h, icon, None, color=color, title=title, **kw)

    def D(x, y, horiz=False):
        if horiz:
            d.bld(OX + x, OY + y, 2, 1, None, None, color=C['door'], op=.9, title='문')
        else:
            d.bld(OX + x, OY + y, 1, 2, None, None, color=C['door'], op=.9, title='문')

    # 바닥·벽 (격벽 안 생활 구역 전체를 타일로 깐 뒤 방을 덮음)

    # --- 서쪽: 개인 침실 3줄 + 현관
    for y in (1, 11, 16):
        for i, x in enumerate((2, 9, 16, 23)):
            R(x, y, 6, 4, '개인', 'bed', size_in_label=True, label_size=8)
            B(x, y + 2, 4, 2, 'Comfy_Bed', '편안한 침대 4×2', '#d9c8a0')
            B(x + 4, y + 3, 1, 1, 'Flower_Pot', '꽃병 (장식)', '#ff9fd0')
            B(x + 5, y + 3, 1, 1, 'Flower_Pot', '꽃병 (장식)', '#ff9fd0')
            if i:
                D(x - 1, y + 2)
        R(30, y, 5, 4, '현관', 'misc', label_size=8)
        D(29, y + 2)
        D(35, y + 2)
    R(11, 6, 24, 4, '주방', 'food', sub='그릴 · 냉장고')
    D(35, 8 - 0)
    R(2, 21, 16, 4, '마사지 클리닉', 'med')
    R(19, 21, 16, 4, '호화 막사', 'barracks')
    for x in (19, 23, 27, 31):
        B(x, 23, 4, 2, 'Comfy_Bed', '편안한 침대 4×2', '#d9c8a0')
    D(18, 23)
    D(35, 23)
    R(11, 26, 24, 4, '실내 목장: 기끌이·잎람쥐', 'ranch', sub='8마리')
    D(35, 28)

    # --- 서쪽 통로: 식물 칸 + 사다리 + 소방서 폴 (자연보호구역)
    d.fill(OX + 36, OY + 0, 3, 30, '#24452e', open=True)
    for y in (5, 10, 15, 20, 25):
        d.fill(OX + 36, OY + y, 1, 1, '#8a6a48')
        d.plants(OX + 36, OY + y - 1, 1, 'Mealwood', title='야생 식물 (자연보호구역)')
    d.ladder(OX + 37, OY + 0, 47)
    d.pole(OX + 38, OY + 0, 47)
    d.fill(OX + 36, OY + 0, 3, 30, 'none', stroke='#acffbd', layer='over')
    D(37, 30, horiz=True)

    # --- 가운데 코어
    R(40, 1, 24, 4, '오락실', 'rec', sub='오락 건물')
    R(40, 6, 24, 5, '복층 큰 회관 (식당)', 'food', sub='위아래 식탁 14 + 워터 쿨러')
    d.tiles(OX + 43, OY + 8, 18, 1, 'tile')          # 가운데 발판
    d.ladder(OX + 42, OY + 6, 5)
    d.ladder(OX + 61, OY + 6, 5)
    for x in (45, 47, 49, 51, 53, 55):
        B(x, 7, 1, 1, 'Mess_Table', '식탁', '#ffe284')
    for x in (44, 46, 48, 50, 52, 54, 56, 58):
        B(x, 10, 1, 1, 'Mess_Table', '식탁', '#ffe284')
    B(57, 6, 2, 2, 'Water_Cooler', '워터 쿨러 (꺼 둠)', '#6aa8ff')
    R(40, 12, 16, 3, '화장실 (세척실)', 'wash', label_size=8)
    for x in (40, 42, 52, 54):
        B(x, 12, 2, 3, 'Sink', '싱크대 2×3', '#9fe8ff')
    for x in (44, 46, 48, 50):
        B(x, 12, 2, 3, 'Lavatory', '수세식 화장실 2×3', '#ffffff')
    R(57, 12, 7, 3, '기계실', 'mech', label_size=8, label_at='bottom')
    B(57, 12, 4, 3, 'Water_Sieve', '물 체 4×3')
    B(61, 13, 1, 2, 'Storage_Bin', '모래 저장통')
    B(62, 12, 1, 3, 'Thimble_Reed', '갈대 (수경 재배)', '#9be36b')
    D(56, 13)
    R(40, 16, 16, 4, '샤워실', 'wash', label_at='bottom')
    for x in range(40, 56, 2):
        B(x, 16, 2, 4, 'Shower', '샤워기 2×4', '#bfe6ff')
    R(57, 16, 7, 4, '여유', 'misc', label_size=8)
    R(40, 21, 24, 4, '포드층 연구실', 'research', sub='포드 + 연구소 + 슈퍼컴')
    B(50, 21, 4, 4, 'Printing_Pod', '프린팅팟 4×4')
    B(42, 23, 2, 2, 'Research_Station', '연구소 2×2', '#e0a0ff')
    B(57, 22, 3, 3, 'Super_Computer', '슈퍼컴퓨터 3×3', '#e0a0ff')
    R(40, 26, 24, 4, '예비 (병원 등)', 'med')
    for y in (3, 9, 13, 18, 23, 28):
        D(39, y)
        D(64, y)

    # --- 동쪽 통로 (사다리 + 소방서 폴)
    d.fill(OX + 65, OY + 0, 2, 30, '#2a2618', open=True)
    d.ladder(OX + 65, OY + 0, 30)
    d.pole(OX + 66, OY + 0, 30)
    for y in (3, 11, 17, 22, 28):
        D(67, y)

    # --- 동쪽: 작업장 · 온실 · 목장 · 수조
    R(68, 1, 16, 4, '작업장', 'misc', sub='저장통 · 제작')
    R(68, 6, 15, 7, '실내 온실 B: 센털꽃', 'farm', sub='센털꽃 24 · 조명 4', label_size=8.5)
    d.ladder(OX + 69, OY + 6, 4)
    d.tiles(OX + 69, OY + 9, 2, 1, 'tile')
    B(69, 10, 2, 3, 'Farm_Station', '재배스테이션 2×3', '#cdf248')
    d.tiles(OX + 71, OY + 9, 12, 1, 'farm')
    d.plants(OX + 71, OY + 8, 12, 'Bristle_Blossom', title='센털꽃')
    d.plants(OX + 71, OY + 12, 12, 'Bristle_Blossom', title='센털꽃')
    d.tiles(OX + 71, OY + 13, 12, 1, 'farm')
    for x, y in ((73, 6), (80, 6), (73, 10), (80, 10)):
        B(x, y, 1, 1, 'Ceiling_Light', '천정등', '#fff6a0')
    R(68, 14, 23, 5, '실내 온실 A: 끼니나무', 'farm', sub='끼니나무 40', label_size=8.5)
    d.ladder(OX + 69, OY + 14, 2)
    d.tiles(OX + 69, OY + 16, 2, 1, 'tile')
    d.tiles(OX + 71, OY + 16, 20, 1, 'farm')
    d.plants(OX + 71, OY + 15, 20, 'Mealwood', title='끼니나무')
    d.tiles(OX + 71, OY + 19, 20, 1, 'farm')
    d.plants(OX + 71, OY + 18, 20, 'Mealwood', title='끼니나무')
    R(68, 20, 24, 4, '실내 목장: 주둥가리', 'ranch', sub='8마리 → 석탄')
    R(68, 26, 30, 4, '깨끗한 물 수조', 'water', sub='30×4 ≈ 120톤', size_in_label=False)
    d.fill(OX + 70, OY + 27, 28, 3, C['water'], op=.6)
    B(68, 28, 2, 2, 'Liquid_Pump', '액체 펌프 2×2')

    # --- 격벽 밖 (아래)
    R(2, 31, 14, 4, '광석·모래 보관', 'misc', dims='wh')
    R(17, 31, 17, 4, '오염된 물 수조', 'water', sub='≈ 68톤', dims='wh')
    d.fill(OX + 17, OY + 32, 17, 3, C['polluted'], op=.7)
    D(16, 33)
    D(35, 33)
    D(39, 33)
    R(40, 31, 24, 4, '발전소', 'ind', sub='석탄 발전기 3×3 ×3', dims='wh')
    for x in (45, 49, 53):
        B(x, 32, 3, 3, 'Coal_Generator', '석탄 발전기 3×3', '#ff9a7a')
    R(65, 31, 14, 4, '정제·제련', 'ind', dims='wh', label_at='bottom', label_size=8)
    B(66, 31, 4, 4, 'Rock_Crusher', '쇄석기 4×4')
    B(71, 31, 3, 4, 'Metal_Refinery', '금속 제련소 3×4', '#ff9a7a')
    R(80, 31, 12, 4, 'SPOM', 'ind', sub='전해조 + 펌프', dims='wh')
    R(93, 31, 8, 4, '수소', 'ind', sub='발전기 4×3 ×2', dims='wh', label_size=8)
    R(5, 36, 12, 8, '헐떡이 목장', 'ranch')
    R(19, 36, 15, 7, '외부 온실: 추운 작물', 'farm', sub='진눈깨비밀·노쉬', label_size=8.5)
    d.ladder(OX + 20, OY + 36, 3)
    d.tiles(OX + 20, OY + 39, 2, 1, 'tile')
    B(20, 40, 2, 3, 'Farm_Station', '재배스테이션 2×3', '#cdf248')
    d.tiles(OX + 22, OY + 39, 12, 1, 'farm')
    d.plants(OX + 22, OY + 38, 12, 'Sleet_Wheat', title='진눈깨비밀')
    d.tiles(OX + 22, OY + 43, 12, 1, 'farm')
    d.plants(OX + 22, OY + 42, 12, 'Sleet_Wheat', title='진눈깨비밀')
    for x, y in ((24, 36), (31, 36), (24, 40), (31, 40)):
        B(x, y, 1, 1, 'Ceiling_Light', '천정등', '#fff6a0')
    D(35, 41)
    R(40, 36, 14, 4, '냉방실', 'cool', sub='열액체조화기 → 증기 터빈')
    D(39, 38)
    R(55, 36, 24, 4, '외부 목장: 미끌이', 'ind', sub='CO₂ 먹음')
    R(88, 36, 10, 8, '가스질 음메', 'ranch')
    R(55, 41, 16, 4, '플록스', 'cool', sub='−30~10°C')
    R(2, 45, 16, 4, '염소 온실', 'farm', sub='아몬나리 · 다샤')
    R(19, 46, 79, 3, 'CO₂ 구덩이 (맨 아래)', 'plan', sub=None)
    d.fill(OX + 19, OY + 46, 79, 3, C['co2'], op=.25)

    # 벽·바닥: 방·통로에 붙은 칸만 타일, 격벽 줄은 절연 타일
    env = set()
    for i in range(OX + 1, OX + 98):
        env |= {(i, OY), (i, OY + 30)}
    for j in range(OY, OY + 31):
        env |= {(OX + 1, j), (OX + 97, j)}
    d.autowalls(OX + 1, OY, 97, 31, 'tile', skip=env)
    d.autowalls(0, OY + 31, 104, 21, 'tile')
    d.tiles(OX + 1, OY, 97, 1, 'ins')
    d.tiles(OX + 1, OY + 30, 97, 1, 'ins')
    d.tiles(OX + 1, OY + 1, 1, 29, 'ins')
    d.tiles(OX + 97, OY + 1, 1, 29, 'ins')
    # 단열 격벽
    d.envelope(OX + 1, OY + 0, 97, 31)

    d.key('env', '단열 격벽 (안쪽 20~25°C)')
    d.key('tile', '절연 타일 (격벽 줄)', 'ins')
    d.key('tile', '타일 (층 바닥·방 사이 벽)', 'tile')
    d.key('icon', '사다리 (올라갈 때)', 'Ladder')
    d.key('icon', '소방서 폴 (내려갈 때, 4배 빠름)', 'Fire_Pole')
    d.key('fill', '문 (2칸)', C['door'])
    d.key('fill', '서쪽 통로 = 식물 칸 + 사다리 + 소방서 폴 (자연보호구역)', '#24452e')
    d.key('room', '침실 (개인 침실 6×4, 호화 막사 16×4)', 'bed')
    d.key('room', '식사 (주방, 큰 회관)', 'food')
    d.key('room', '화장실·샤워실', 'wash')
    d.key('room', '농장', 'farm')
    d.key('room', '목장', 'ranch')
    d.key('room', '산업 (격벽 밖)', 'ind')
    d.key('room', '물 수조', 'water')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d




def early():
    d = BP('core-base-early', cols=104, rows=40, unit=11, x0=OX, y0=OY, label_every=5,
           title='초반 임시 배치 (사이클 1~20, 1칸 = 1타일)', legend_cols=3,
           note='벽·바닥 줄은 처음부터 후반 도면 위치에 놓습니다. 점선 방 = 아직 안 판 곳(후반 용도), 노란 점선 = 나중에 단열 격벽을 두를 선.\n'
                '식당은 24×5를 다 파 두되 13번째 칸에 임시 벽 → 왼쪽 12×5 = 60칸만 식당 (식당 최대 64칸).')

    def R(x, y, w, h, name, kind, sub=None, dims='wh', **kw):
        d.room(OX + x, OY + y, w, h, name, kind, sub=sub, dims=dims, **kw)

    def P(x, y, w, h, name, **kw):
        d.room(OX + x, OY + y, w, h, name + ' 자리', 'plan', dims='', dashed=True, label_size=8, **kw)

    def B(x, y, w, h, icon, title=None, color='#c0c8e0', **kw):
        d.bld(OX + x, OY + y, w, h, icon, None, color=color, title=title, **kw)

    def D(x, y):
        d.bld(OX + x, OY + y, 1, 2, None, None, color=C['door'], op=.9, title='문')

    for y in (1, 11, 16):
        for x in (2, 9, 16, 23):
            P(x, y, 6, 4, '개인')
    P(40, 1, 24, 4, '오락실')
    P(40, 16, 24, 4, '샤워실')
    P(57, 12, 7, 3, '기계실')
    P(2, 21, 16, 4, '마사지 클리닉')
    P(11, 26, 24, 4, '목장')
    P(68, 1, 16, 4, '작업장')
    P(68, 6, 15, 7, '온실 B')
    P(68, 20, 24, 4, '주둥가리 목장')
    P(80, 31, 21, 4, 'SPOM·수소')
    P(17, 31, 17, 4, '오염된 물 수조')
    P(2, 31, 14, 4, '보관')

    R(11, 6, 24, 4, '보관·조리', 'misc', sub='분쇄기 · 배급 상자 (나중에 주방)')
    B(13, 8, 2, 2, 'Microbe_Musher', '미생물 걸죽기 2×2')
    B(16, 9, 1, 1, 'Ration_Box', '배급 상자')
    B(18, 8, 1, 2, 'Storage_Bin', '보관함')
    R(40, 6, 12, 5, '식당', 'food', sub='식탁 4', dims='h')
    d.dim(OX + 40, OX + 52, OY + 5.5)
    d.tiles(OX + 52, OY + 6, 1, 5, 'tile')     # 임시 벽 (13번째 칸)
    d.fill(OX + 52, OY + 6, 1, 5, 'none', stroke='#ffe284', dash=True, layer='over')
    d.room(OX + 53, OY + 6, 11, 5, '나중에 복층', 'plan', dims='', dashed=True, label_size=8, size_in_label=False)
    d.mark_open(OX + 53, OY + 6, 11, 5)
    d.dim(OX + 40, OX + 64, OY + 4.5, '파 둘 칸 24')
    for x in (44, 46, 48, 50):
        B(x, 10, 1, 1, 'Mess_Table', '식탁', '#ffe284')
    R(40, 12, 16, 3, '화장실', 'wash', sub=None, label_size=8)
    for x in (42, 46):
        B(x, 12, 2, 3, 'Wash_Basin', '세면기 2×3', '#9fe8ff')
    for x in (44, 48):
        B(x, 12, 2, 3, 'Outhouse', '뒷간 2×3', '#c8a070')
    R(40, 21, 24, 4, '포드층', 'misc', sub='포드 + 연구소 + 수동 발전기')
    B(50, 21, 4, 4, 'Printing_Pod', '프린팅팟 4×4')
    B(42, 23, 2, 2, 'Research_Station', '연구소 2×2', '#e0a0ff')
    B(58, 23, 2, 2, 'Manual_Generator', '수동 발전기 2×2', '#f4a442')
    R(19, 21, 16, 4, '막사 → 호화 막사', 'barracks', sub='간이 침대 3')
    for x in (19, 21, 23):
        B(x, 23, 2, 2, 'Cot', '간이 침대 2×2', '#d9c8a0')
    R(68, 14, 23, 5, '실내 온실 A 자리: 재배 타일 한 줄', 'farm', sub='끼니나무 20 (4명)', label_size=8.5, size_in_label=False)
    d.tiles(OX + 71, OY + 19, 20, 1, 'farm')
    d.plants(OX + 71, OY + 18, 20, 'Mealwood', title='끼니나무')
    d.ladder(OX + 69, OY + 14, 5)
    R(68, 26, 30, 4, '웅덩이 → 수조', 'water', sub='펌프', size_in_label=False)
    d.fill(OX + 70, OY + 28, 26, 2, C['water'], op=.6)
    R(40, 26, 24, 4, '산소 확산기 · 펌프 (임시)', 'misc', sub='나중에 예비 (병원 등)', size_in_label=False)
    B(44, 28, 1, 2, 'Oxygen_Diffuser', '산소 확산기 1×2', '#7ad97a')
    R(40, 31, 24, 4, '발전소', 'ind', sub='석탄 발전기 1 + 배터리 2')
    B(45, 32, 3, 3, 'Coal_Generator', '석탄 발전기 3×3', '#ff9a7a')
    B(57, 33, 1, 2, 'Battery', '배터리 1×2', '#5fd0ff')
    B(58, 33, 1, 2, 'Battery', '배터리 1×2', '#5fd0ff')
    R(65, 31, 14, 4, '정제', 'mech', sub='쇄석기', label_at='top')
    B(66, 31, 4, 4, 'Rock_Crusher', '쇄석기 4×4')

    d.fill(OX + 36, OY + 0, 3, 30, '#24452e', open=True)
    for y in (5, 10, 15, 20, 25):
        d.fill(OX + 36, OY + y, 1, 1, '#8a6a48')
        d.plants(OX + 36, OY + y - 1, 1, 'Mealwood', title='야생 식물 (공원 → 자연보호구역)')
    d.ladder(OX + 37, OY + 0, 35)
    d.pole(OX + 38, OY + 0, 35)
    d.fill(OX + 36, OY + 0, 3, 30, 'none', stroke='#acffbd', layer='over')
    d.fill(OX + 65, OY + 10, 2, 20, '#2a2618', open=True)
    d.ladder(OX + 65, OY + 10, 20)
    d.pole(OX + 66, OY + 10, 20)
    for y in (9, 13, 18, 23, 28):
        D(39, y)
        D(64, y)
    D(35, 8)
    D(35, 23)
    D(67, 17)
    D(39, 33)

    d.autowalls(0, 0, 104, 40, 'tile')
    d.envelope(OX + 1, OY + 0, 97, 31)

    d.key('env', '나중에 단열 격벽을 두를 선')
    d.key('room', '아직 안 판 곳 (후반 용도)', 'plan')
    d.key('tile', '타일 (지은 벽·바닥)', 'tile')
    d.key('icon', '사다리', 'Ladder')
    d.key('icon', '소방서 폴', 'Fire_Pole')
    d.key('fill', '문 (2칸)', C['door'])
    d.key('fill', '서쪽 통로 (공원 → 자연보호구역)', '#24452e')
    d.key('icon', '뒷간 + 세면기 번갈아 2개씩', 'Outhouse')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def build():
    return [late(), early()]
