from bp import BP, C

CL = '#c8e04a'   # 염소
MIX = '#c9a0ff'  # 섞인 공기 (입구)


def gas_sorter():
    d = BP('gas-sorter', cols=17, rows=21, unit=24, x0=0, y0=0, title='필터 없는 기체 분리탑 (밀도 분리) 3×14',
           legend_cols=2, show_zero=False,
           note='원리: 몰 질량 수소 1.0 < 산소·오염된 산소 16.0 < 염소 34.5 < CO₂ 44.0 (위키 Gas). 가벼운 기체가 위, 무거운 기체가 아래로 층을 이룸.\n'
                '필터·원소 센서·무한 저장(액체 속 배출구) 없음. 미니 기체 펌프 5대(입구 포함) × 60 W, 각 50 g/s.\n'
                '입구는 50 g/s 이하로. 층이 비면 그 펌프는 옆 층을 빨아들임 → 수소 줄은 위쪽 수소 포켓을 한 번 더 거침(2단 분리).\n'
                '염소 줄은 기체 브리지로 CO₂ 덤프 줄에 합류: 브리지 출구가 줄을 따라 오는 흐름보다 우선\n'
                '(Klei 포럼 · Pipes & Bridges Priority Cheat Sheet, kleiforums.com/forums/topic/102326).\n'
                '산소와 오염된 산소는 무게가 같아서 이 탑으로는 안 나뉨 (둘 다 기지로 되돌림).')
    T = d.tiles
    # 벽 (안쪽 3×14, 바깥 5×16)
    T(4, 2, 5, 1); T(4, 17, 5, 1); T(4, 3, 1, 14); T(8, 3, 1, 14)
    d.room(5, 3, 3, 14, None, 'gasroom', dims='wh', dim_w_at=2.5, dim_h_at=3.5)
    # 층
    d.fill(5, 3, 3, 2, C['h2'], op=.45)
    d.fill(5, 5, 3, 8, C['o2'], op=.22)
    d.fill(5, 13, 3, 2, CL, op=.45)
    d.fill(5, 15, 3, 2, C['co2'], op=.55)
    for y, s, col in ((4.1, '수소', C['h2']), (8.2, '산소·오염된 산소', C['o2']), (14.1, '염소', CL), (16.1, 'CO₂', '#d0d0d0')):
        d.text(6.5, y, s, col, 9.5, bold=True, halo=True)
    # 건물
    d.bld(5, 3, 1, 2, 'Mini_Gas_Pump', None, color=C['h2'], op=.4, title='P1 미니 기체 펌프 (수소)')
    d.bld(7, 6, 1, 2, 'Mini_Gas_Pump', None, color=C['o2'], op=.4, title='P2 미니 기체 펌프 (산소 되돌림)')
    d.bld(5, 9, 1, 1, 'Gas_Vent', None, color=MIX, op=.5, title='입구 기체 배출구 (섞인 공기)')
    d.bld(7, 13, 1, 2, 'Mini_Gas_Pump', None, color=CL, op=.4, title='P3 미니 기체 펌프 (염소)')
    d.bld(5, 15, 1, 2, 'Mini_Gas_Pump', None, color=C['co2'], op=.5, title='P4 미니 기체 펌프 (CO₂)')
    d.bld(10, 16, 1, 3, 'Gas_Bridge', None, color=CL, op=.35, title='기체 브리지 (염소 → 덤프 줄, 우선)')
    d.bld(0, 8, 1, 2, 'Mini_Gas_Pump', None, color=MIX, op=.4, title='P0 입구 펌프 (기지 가장 낮은 칸)')
    for x, y, s in ((5.5, 2.6, 'P1'), (7.5, 5.6, 'P2'), (7.5, 12.6, 'P3'), (5.5, 14.6, 'P4'), (0.5, 7.6, 'P0'), (10.5, 15.6, '브리지')):
        d.text(x, y, s, C['ink'], 9, bold=True, halo=True)
    # 파이프
    d.line([(0, 9), (5, 9)], MIX, arrow=True)
    d.line([(5, 3), (5, 0), (16, 0)], C['h2'], arrow=True)
    d.line([(7, 6), (16, 6)], C['o2'], arrow=True)
    d.line([(7, 13), (10, 13), (10, 16)], CL)
    d.line([(5, 15), (5, 18), (16, 18)], C['co2'], arrow=True)
    d.extra_right = 190
    X = d.X(17) + 6
    d.text(X, d.Y(0.5) + 4, '→ 위쪽 수소 포켓 → 수소 발전기', C['h2'], 10, anchor='start', raw=True)
    d.text(X, d.Y(6.5) + 4, '→ 기지로 되돌림 (기체 배출구)', C['o2'], 10, anchor='start', raw=True)
    d.text(X, d.Y(18.5) + 4, '→ 덤프: 기지보다 낮은 웅덩이', '#d0d0d0', 10, anchor='start', raw=True)
    d.text(X, d.Y(18.5) + 18, '   (염소 + CO₂, 무거워서 안 올라옴)', C['dim'], 10, anchor='start', raw=True)
    d.text(d.X(0) + 2, d.Y(11) - 4, '← 기지 공기', MIX, 9.5, anchor='start', raw=True)
    d.vdim(9.5, 3, 5, '2')
    d.vdim(9.5, 13, 17, '4')
    d.key('tile', '타일 (밀폐 벽)', 'tile')
    d.key('icon', '미니 기체 펌프 1×2 · 60 W · 50 g/s', 'Mini_Gas_Pump')
    d.key('line', '섞인 공기 (입구)', MIX)
    d.key('icon', '기체 브리지 1×3', 'Gas_Bridge')
    d.key('line', '수소 줄', C['h2'])
    d.key('line', '산소·오염된 산소 줄 (되돌림)', C['o2'])
    d.key('line', '염소 줄', CL)
    d.key('line', 'CO₂ 덤프 줄', C['co2'])
    d.key('dim', '치수선 (칸 수)')
    return d


def build():
    return [gas_sorter()]
