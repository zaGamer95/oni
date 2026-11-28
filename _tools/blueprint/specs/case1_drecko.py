from bp import BP, C


def build():
    # 목장 바깥 벽 기준 22×11. 왼쪽 1칸(치수선), 위 1칸(수소 파이프), 아래 2칸(액체 잠금 바닥·전체 치수)을 여백으로 둠.
    d = BP('case1-drecko-ranch', cols=24, rows=14, unit=24, x0=1, y0=1, title='기끌이 목장 22×11 (2층) · 칸별 도면',
           note='2LegitCity 영상 구조를 칸 단위로 옮긴 계획안. 건물 크기는 위키 기준(털깎이 3×3, 치장스테이션 2×3, 투입구 1×3, 슈트 거치대·검문소 1×3).\n'
                '축사 = 위층 12×4(48) + 아래층 11×4(44) + 층 사이 구멍 2 = 94칸 (축사 한도 96 이하) → 기끌이 7마리(12칸씩).')
    o = 1  # 바깥 벽 왼쪽 위 = (1, 1)

    def T(x, y, w, h, k='tile'):
        d.tiles(o + x, o + y, w, h, k)

    # 벽·바닥 (바깥 22×11 + 액체 잠금 아래 1줄)
    T(0, 0, 22, 1)
    T(0, 10, 22, 1)
    T(0, 1, 1, 9, 'ins')      # 서쪽 벽 = 절연 타일 (분출구 쪽)
    T(21, 1, 1, 7)
    T(13, 1, 1, 4)            # 위층 칸막이 (전해조 방)
    T(12, 6, 2, 2)
    T(13, 8, 1, 1)            # 액체 잠금 가운데 천장 (물에 잠김)
    T(11, 11, 5, 1)           # 액체 잠금 바닥
    T(11, 10, 1, 1)
    T(15, 10, 1, 1)
    d.tiles(o + 1, o + 5, 20, 1, 'mesh')   # 층 사이 메시 타일

    # 방
    d.room(o + 1, o + 1, 12, 4, '위층 축사 (수소)', 'gasroom', dims='wh')
    d.room(o + 14, o + 1, 7, 4, '전해조 방', 'misc', dims='w', label_at='bottom')
    d.room(o + 1, o + 6, 11, 4, '아래층 축사', 'gasroom', dims='h', label_at='top')
    d.dim(o + 1, o + 12, o + 10.5)
    d.fill(o + 1, o + 8, 11, 2, '#1f4a5a', op=.85)          # 산소·CO2 층
    d.room(o + 14, o + 6, 7, 4, '슈트 현관', 'misc', dims='', label_at='top')
    d.fill(o + 1, o + 5, 1, 1, '#3a2f55')                    # 층 사이 구멍
    d.fill(o + 11, o + 5, 1, 1, '#3a2f55')
    # 액체 잠금 (U자)
    d.fill(o + 12, o + 8, 1, 1, '#1f4a5a')
    d.fill(o + 14, o + 8, 1, 1, '#30344a')
    d.fill(o + 12, o + 9, 3, 2, C['water'])

    # 건물
    d.bld(o + 2, o + 2, 1, 3, 'Critter_Drop-Off', '투입', color='#e07a3a', label_pos='above')
    d.bld(o + 4, o + 2, 3, 3, 'Shearing_Station', '털깎이', color='#c9a0ff')
    d.bld(o + 8, o + 2, 2, 3, 'Grooming_Station', '손질', color='#ffd166')
    d.bld(o + 10, o + 3, 2, 2, 'Sweepy_Dock', '청소', color='#8fd3ff')
    d.bld(o + 12, o + 3, 1, 2, 'Storage_Bin', None, color='#bbbbbb', title='보관함')
    d.bld(o + 7, o + 1, 1, 1, 'Gas_Vent', None, color=C['h2'], title='기체 배출구 (수소)')
    d.bld(o + 14, o + 1, 2, 2, 'Gas_Pump', 'H₂', color=C['h2'])
    d.bld(o + 16, o + 3, 2, 2, 'Electrolyzer', None, color='#5fd0ff', title='전해조')
    d.bld(o + 19, o + 3, 2, 2, 'Gas_Pump', 'O₂', color=C['o2'])
    d.plants(o + 2, o + 8, 8, 'Mealwood', title='끼니나무')
    d.tiles(o + 2, o + 9, 8, 1, 'farm')
    d.bld(o + 16, o + 7, 1, 3, 'Atmo_Suit_Checkpoint', None, color='#ffe284', title='슈트 검문소')
    for i in range(3):
        d.bld(o + 17 + i, o + 7, 1, 3, 'Atmo_Suit_Dock', None, color='#9fb7ff', title='대기 슈트 거치대')
    d.door(o + 21, o + 8)
    d.ladder(o + 11, o + 5, 5)
    d.ladder(o + 20, o + 5, 3)

    # 파이프
    d.line([(o + 15, o + 1), (o + 15, 0), (o + 7, 0), (o + 7, o + 1)], 'h2')
    d.bld(o + 10.5, -0.0, 1, 1, 'Gas_Shutoff', None, color='#ffe284', title='기체 차단 밸브 (한 번 채우면 잠금)', op=.5)
    d.line([(o + 19.5, o + 3.5), (o + 22.6, o + 3.5)], 'o2', arrow=True)
    d.line([(o + 22.6, o + 4.3), (o + 17, o + 4.3)], 'liquid', dash='6 3', arrow=True)
    d.extra_right = 190
    X = d.X(24) + 6
    d.text(X, d.Y(o + 3.5) + 4, 'O₂ → 아래층 바닥, 남으면 밖으로', C['o2'], 10, anchor='start', raw=True)
    d.text(X, d.Y(o + 4.3) + 14, '물 ← 분출구 옆 웅덩이', C['liquid'], 10, anchor='start', raw=True)

    # 전체 치수 (바깥 벽 포함)
    d.dim(o, o + 22, o + 12.5, '바깥 22')
    d.vdim(o - .5, o, o + 11, '바깥 11')

    d.key('room', '축사 (위층은 수소로 채움, 기끌이 비늘이 자라는 층)', 'gasroom')
    d.key('fill', '산소·CO₂ (무거워 아래로 가라앉음, 끼니나무 호흡용)', '#1f4a5a')
    d.key('tile', '타일 (벽·바닥)', 'tile')
    d.key('tile', '절연 타일 (서쪽 벽, 분출구 쪽)', 'ins')
    d.key('tile', '메시 타일 (층 사이, 기체는 통과)', 'mesh')
    d.key('tile', '재배 타일 + 끼니나무 8그루', 'farm')
    d.key('fill', '액체 잠금: U자 물, 14번 칸 천장이 잠김', C['water'])
    d.key('line', '수소 기체 파이프 → 천장 배출구 (채우면 밸브 잠금)', 'h2')
    d.key('icon', '대기 슈트 거치대 ×3 + 검문소 (안은 수소라 슈트 필요)', 'Atmo_Suit_Dock')
    d.key('dim', '치수선 = 방 안쪽 칸 수 (벽 제외)')
    return [d]
