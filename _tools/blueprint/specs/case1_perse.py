from bp import BP, C


def bedrooms():
    # x: 0 = 서쪽 사다리, 1~26 = 코어(문 칸 포함 26칸), 27 = 가운데 통로 사다리
    # y: 0 = 기지 지붕, 1~4 위층, 5 발판, 6~9 아래층, 10 발판(큰 회관 천장), 11~12 큰 회관
    d = BP('case1-perse-bedrooms', cols=28, rows=13, unit=24, x0=1, y0=0, show_zero=True,
           title='Persephazon 본진 · 큰 회관 위 2개 층 개인 침실 6칸',
           note='층·발판은 지금 그대로. 방끼리 문으로 이어 붙여 남의 방을 지나다님 (잠은 빛·Loud Sleeper만 깨움).\n'
                '아래층 서쪽 수동 발전기·배터리는 먼저 기지 밖으로 옮김 (산업 기계가 있으면 침실이 안 됨). 7·8번째 복제체는 서쪽 기존 간이 침대 2개.\n'
                '가로 26칸은 사이클 160 스크린샷에서 잰 값 (W 확인: 큰 회관 플랫폼 26칸).')
    d.tiles(0, 0, 28, 1, 'ins')
    d.ladder(0, 1, 12)
    d.ladder(27, 1, 12)
    d.tiles(1, 5, 26, 1)
    d.tiles(1, 10, 26, 1)
    n = 1
    for y in (1, 6):
        x = 1
        for w in (6, 6, 10):
            d.tiles(x, y, 1, 2)
            d.door(x, y + 2)
            x += 1
            d.room(x, y, w, 4, '침실 %d' % n, 'bed', dims='w' if y == 1 else '', label_at='top',
                   dim_w_at=y + 4.5 if y == 6 else None, size_in_label=True)
            d.bld(x + 1, y + 2, 4, 2, 'Comfy_Bed', None, color='#e7b45a', title='편안한 침대 4×2 (전엔 간이 침대)')
            d.icon(x + w - 2, y, 1, 2, 'Hanging_Pot', title='매달린 단지 (장식 1)')
            d.icon(x + w - 1, y, 1, 2, 'Hanging_Pot', title='매달린 단지 (장식 2)')
            x += w
            n += 1
        d.tiles(x, y, 1, 2)
        d.door(x, y + 2)
    d.room(1, 11, 26, 2, '큰 회관 (그대로) → 아래 화장실 → 샤워실 → 포드', 'food', dims='', label_at='mid', size_in_label=False)
    d.key('room', '개인 침실 (6×4 = 24칸, 끝 방 10×4 = 40칸) · 뒷벽 건식벽체 전부', 'bed')
    d.key('icon', '편안한 침대 4×2 (플라스틱 200 kg) · 전엔 간이 침대 = 막사 +1', 'Comfy_Bed')
    d.key('icon', '매달린 단지 2개 = 장식 2개 (식물이 한 칸 아래로)', 'Hanging_Pot')
    d.key('icon', '문 (양 끝은 사다리, 가운데는 옆 방으로)', 'Pneumatic_Door')
    d.key('tile', '절연 타일 (기지 지붕)', 'ins')
    d.key('icon', '사다리 (서쪽 · 가운데 통로)', 'Ladder')
    d.key('dim', '치수선 (칸)')
    return d


def hospital():
    # x: 0 = 텔레포터 쪽, 1 서쪽 벽(문), 2~17 병원 16칸, 18 동쪽 벽(문), 19 서쪽 사다리
    d = BP('case1-perse-hospital', cols=20, rows=6, unit=26, x0=2, y0=1,
           title='Persephazon 병원 · 텔레포터 오른쪽 빈 16×4 방',
           note='병원 조건 (위키): 12~96칸, 의료 침대 1개 이상, 화장실 1개(꺼 둬도 됨), 식탁 1개, 산업 기계 없음.\n'
                '병원 안 화장실·식탁은 입원한 복제체만 씀. 병상은 Bedside Manner(간호) 스킬 복제체가 있어야 씀.')
    d.tiles(0, 0, 20, 1, 'ins')
    d.tiles(0, 5, 20, 1, 'ins')
    d.fill(0, 1, 1, 4, '#2a3550')
    d.text(.5, 1.9, '텔레', '#cfe0ff', 9); d.text(.5, 2.4, '포터', '#cfe0ff', 9)
    d.tiles(1, 1, 1, 2, 'ins')
    d.door(1, 3)
    d.tiles(18, 1, 1, 2, 'ins')
    d.door(18, 3)
    d.ladder(19, 1, 4)
    d.room(2, 1, 16, 4, '병원 (Hospital)', 'med', dims='wh', label_at='top')
    d.bld(2, 3, 3, 2, 'Triage_Cot', '부상자분류 간이침대', color='#ff848e')
    d.bld(5, 3, 3, 2, 'Triage_Cot', '부상자분류 간이침대', color='#ff848e')
    d.bld(8, 3, 3, 2, 'Sick_Bay', '병상', color='#ffb3b9')
    d.bld(11, 2, 2, 3, 'Outhouse', '화장실(끔)', color='#c0c8e0')
    d.bld(13, 4, 1, 1, 'Mess_Table', None, color='#ffe284', title='식탁 (방 조건용)')
    d.bld(14, 2, 4, 3, None, '나중: 질병 클리닉 2×3', color='#a9b0d0', planned=True, fs=8.5)
    d.icon(4, 1, 1, 1, 'Ceiling_Light', title='천정등 1개')
    d.key('room', '병원 16×4 = 64칸 (12~96칸)', 'med')
    d.key('icon', '부상자분류 간이침대 3×2: 체력 +50/사이클 (돌봄 받으면 +75), 쓰러진 복제체를 되살림', 'Triage_Cot')
    d.key('icon', '병상 3×2: 는지렁이허파 치료, 의료 팩 1 kg/회 (Medical Equipment 연구)', 'Sick_Bay')
    d.key('icon', '뒷간 2×3: 꺼 둠 (방 조건만 채움)', 'Outhouse')
    d.key('icon', '식탁 1×1 (방 조건)', 'Mess_Table')
    d.key('tile', '절연 타일 (지금 있는 벽·바닥)', 'ins')
    d.legend_cols = 1
    return d


def build():
    return [bedrooms(), hospital()]
