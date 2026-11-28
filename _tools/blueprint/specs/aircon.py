from bp import BP, C


def aircon():
    ox, oy = 2, 1
    d = BP('aircon-room', cols=19, rows=11, unit=26, x0=ox + 1, y0=oy, title='냉방실 14×4 (+ 위 3칸 증기 터빈 자리)',
           legend_cols=2,
           note='열액체조화기는 바닥 오른쪽(10~11번), 터빈은 왼쪽 위(2~6번). 터빈은 절연 타일 줄 위에 앉고, 그 줄 바로 아래 5칸에서 증기를 빨아들임.\n'
                '벽·천장·바닥 = 절연 타일 (16×6 테두리). 오염된 물 ≈ 20톤 = 바닥 1줄 14칸 + 둘째 줄 6칸.')
    T = lambda x, y, w, h, k='ins': d.tiles(ox + x, oy + y, w, h, k)
    T(0, 0, 16, 1)            # 격벽 줄 (위 = 생활 구역)
    T(0, 1, 1, 3); T(15, 1, 1, 3)
    T(0, 4, 16, 1)            # 터빈 받침 = 냉방실 천장
    T(0, 5, 1, 4); T(15, 5, 1, 4)
    T(0, 9, 16, 1)
    d.room(ox + 1, oy + 1, 14, 3, '터빈 자리', 'plan', dims='', dashed=True, label_at='bottom', size_in_label=False)
    d.mark_open(ox + 1, oy + 1, 14, 3)
    d.room(ox + 1, oy + 5, 14, 4, '냉방실', 'cool', dims='wh', label_at='top', dim_w_at=oy + 9.5, dim_h_at=ox + 16.5)
    d.fill(ox + 1, oy + 8, 14, 1, C['polluted'], op=.9)
    d.fill(ox + 1, oy + 7, 6, 1, C['polluted'], op=.9)
    d.bld(ox + 2, oy + 1, 5, 3, 'Steam_Turbine', '증기 터빈 5×3 (7단계)', color='#8a9bd0', planned=True)
    for i in range(5):
        d.text(ox + 2.5 + i, oy + 5.75, '⋀', '#c9d1f0', 12, bold=True)
    d.bld(ox + 10, oy + 7, 2, 2, 'Thermo_Aquatuner', '수냉', color='#e0b060', op=.5, title='열액체조화기 2×2 · 1,200 W')
    d.bld(ox + 7, oy + 5, 1, 1, 'Liquid_Vent', None, color='#ffe284', title='액체 배출구 (터빈 95°C 물)')
    c = lambda x, y: (ox + x, oy + y)
    d.line([c(8, 0), c(8, 1)], 'ins_hot')
    d.line([c(8, 1), c(2, 1)], '#ff5c8a', w=5)
    d.line([c(2, 1), c(1, 1), c(1, 6), c(10, 6), c(10, 7)], 'ins_hot')
    d.line([c(11, 7), c(11, 6), c(12, 6), c(12, 0)], 'ins_cold')
    d.line([c(6, 3), c(7, 3), c(7, 5)], 'wire', w=3)
    d.line([(0.3, oy + 8.5), (ox + 10, oy + 8.5)], 'auto', dash='7 4', w=3, center=False)
    d.bld(ox + 0, oy + 8, 1, 1, 'Heavi-Watt_Joint_Plate', None, color='#acffbd', op=.6, title='헤비와트 연결판 (벽 통과)')
    d.extra_right = 150
    X = d.X(19) + 6
    d.text(X, d.Y(oy + .5) + 4, '↑ 기지로 (차가움)', C['cold'], 10, anchor='start', raw=True)
    d.text(X, d.Y(oy + .5) + 18, '↓ 기지에서 (18°C+)', C['heat'], 10, anchor='start', raw=True)
    d.text(X, d.Y(oy + 4.5) + 4, '천장 = 절연 타일', C['ink'], 10, anchor='start', raw=True)
    d.text(X, d.Y(oy + 6) + 4, '공기·증기층', C['dim'], 10, anchor='start', raw=True)
    d.text(X, d.Y(oy + 8.5) + 4, '오염된 물 약 20톤', '#8fe3ff', 10, anchor='start', raw=True)
    d.text(d.X(0) + 2, d.Y(oy + 8.5) - 8, '발전소 ←', '#acffbd', 9.5, anchor='start', raw=True)
    d.vdim(ox + 15.5 + 1, oy + 1, oy + 4, '터빈 3')
    d.key('tile', '절연 타일 (격벽·냉방실 벽)', 'ins')
    d.key('fill', '오염된 물 (바닥 1줄 + 6칸 ≈ 20톤)', C['polluted'])
    d.key('ins', '돌아오는 냉각수: 절연 액체 파이프', 'heat')
    d.key('line', '방사형 액체 파이프 (터빈 식히기, 7단계 때)', '#ff5c8a')
    d.key('ins', '식은 냉각수: 절연 액체 파이프 → 기지', 'cold')
    d.key('line', '터빈이 내보내는 95°C 물 → 액체 배출구', 'wire')
    d.key('dash', '헤비와트 와이어 (벽은 연결판으로)', 'auto')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def build():
    return [aircon()]
