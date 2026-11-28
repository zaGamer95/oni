from bp import BP, C


def hatch_ranch():
    d = BP('hatch-ranch', cols=29, rows=7, unit=26, x0=3, y0=1, title='실내 목장: 주둥가리 24×4 = 96칸 (8마리 × 12칸)',
           legend_cols=2,
           note='1~2번 치장스테이션 · 3번 사료 공급기 · 4번 크리터 투하 · 8번 아래 두 칸에 공압문(자동) = 주둥가리 울타리.\n'
                '문 위 두 칸은 뚫려 있어 방은 안 나뉨 · 주둥가리는 2칸 높이를 못 넘고 자동 문은 통과 안 함 → 9~24번은 못 오지만 방 칸 수(96)에 들어감.\n'
                '알은 바로 방 밖 보관함으로 수거 → 필요한 만큼만 부화 · 석탄은 발전소로 바로.')
    oy = 1
    d.fill(0, oy + 0, 2, 6, '#2a2618')
    d.ladder(0, oy + 0, 6)
    d.pole(1, oy + 0, 6)
    d.tiles(2, oy + 0, 26, 1)
    d.tiles(2, oy + 5, 26, 1)
    d.tiles(2, oy + 1, 1, 4)
    d.tiles(27, oy + 1, 1, 4)
    d.room(3, oy + 1, 24, 4, '주둥가리 목장', 'ranch', dims='wh', label_at='top', dim_w_at=oy + 5.5)
    d.door(2, oy + 3)
    d.bld(3, oy + 2, 2, 3, 'Grooming_Station', '손질', color='#e8c070', title='치장스테이션 2×3')
    d.bld(5, oy + 3, 1, 2, 'Critter_Feeder', None, color='#f4a442', title='크리터 사료 공급기 1×2')
    d.bld(6, oy + 2, 1, 3, 'Critter_Drop-Off', None, color='#8fe3ff', title='크리터 투하 1×3')
    d.bld(10, oy + 3, 1, 2, 'Pneumatic_Door', '자동문', color='#ff8a4c', op=.45, title='공압문 (자동) = 울타리', label_pos='above')
    for x, y in ((7, 4), (8, 4), (9, 4), (7, 3), (8, 3), (9, 3), (8, 2), (9, 2)):
        d.icon(x + .05, oy + y + .1, .9, .9, 'Hatch', title='주둥가리')
    d.fill(3, oy + 1, 8, 4, 'none', stroke='#ff8a4c', dash=True, layer='over')
    d.dim(3, 11, oy + .5, '주둥가리 자리 8')
    d.key('icon', '주둥가리 8마리 (울타리 안 1~7번)', 'Hatch')
    d.key('icon', '공압문(자동) = 울타리, 위 2칸은 뚫림', 'Pneumatic_Door')
    d.key('icon', '치장스테이션 2×3', 'Grooming_Station')
    d.key('icon', '크리터 사료 공급기 1×2 · 크리터 투하 1×3', 'Critter_Feeder')
    d.key('tile', '지은 바닥·벽 타일', 'tile')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def build():
    return [hatch_ranch()]
