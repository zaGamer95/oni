from bp import BP, C


def corridor():
    # 서쪽 방(4칸만 보임) | 벽 | 식물·사다리·소방봉 | 벽 | 동쪽 방(2칸만 보임), 두 층
    d = BP('core-corridor', cols=13, rows=13, unit=28, x0=1, y0=1, title='서쪽 통로 단면 두 층 (1칸 = 1타일)', legend_cols=1,
           note='통로 3칸 = 식물 칸 1 + 사다리 1 + 소방봉 1. 층 = 내부 4칸 + 바닥 1칸.')
    ox, oy = 1, 1
    W = lambda x, y, w, h, k='tile': d.tiles(ox + x, oy + y, w, h, k)
    for y in (0, 5, 10):
        W(0, y, 5, 1)
        W(8, y, 3, 1)
    W(4, 1, 1, 4); W(4, 6, 1, 4); W(8, 1, 1, 4); W(8, 6, 1, 4)
    d.room(ox + 0, oy + 1, 4, 4, '서쪽 방', 'barracks', dims='', size_in_label=False)
    d.room(ox + 0, oy + 6, 4, 4, None, 'barracks', dims='h')
    d.room(ox + 9, oy + 1, 2, 4, '동쪽', 'wash', dims='', size_in_label=False)
    d.room(ox + 9, oy + 6, 2, 4, None, 'wash', dims='')
    d.fill(ox + 5, oy + 0, 3, 11, '#24452e')
    for y in (5, 10):
        d.fill(ox + 5, oy + y, 1, 1, '#8a6a48')
    d.plants(ox + 5, oy + 4, 1, 'Mealwood', title='야생 식물 (잎람쥐가 심음)')
    d.plants(ox + 5, oy + 9, 1, 'Mealwood', title='야생 식물')
    d.icon(ox + 5, oy + 6, 1, 1, 'Mirth_Leaf', title='자연 타일 아래 매달린 식물 (예시)')
    d.bld(ox + 5, oy + 1, 1, 1, None, '표', color='#e8d080', op=.8, title='공원 표지판 (1개면 충분)', fs=11)
    d.ladder(ox + 6, oy + 0, 11)
    d.pole(ox + 7, oy + 0, 11)
    d.fill(ox + 5, oy + 0, 3, 11, 'none', stroke='#acffbd', layer='over')
    for x in (4, 8):
        for y in (3, 8):
            d.door(ox + x, oy + y)
    d.dim(ox + 5, ox + 8, oy - .5, '통로 3')
    d.vdim(ox + 11.5, oy + 5, oy + 10, '층 5')
    d.dim(ox + 0, ox + 4, oy + 10.5 + 1, '4')
    d.key('fill', '초록 테두리 = 통로 전체가 방 1개 (자연보호구역)', '#24452e')
    d.key('fill', '갈색 = 파지 않고 남긴 자연 타일 (층 바닥 줄)', '#8a6a48')
    d.key('icon', '그 위 야생 식물 (잎람쥐가 심음)', 'Mealwood')
    d.key('icon', '자연 타일 아래 매달린 식물', 'Mirth_Leaf')
    d.key('fill', '표 = 공원 표지판 1개면 충분', '#e8d080')
    d.key('fill', '문 = 층마다 양쪽 (방 경계)', C['door'])
    d.key('tile', '벽·바닥 타일', 'tile')
    return d


def _wash(d, ox, oy, zoom=False):
    """화장실층 + 샤워실층.
    로컬 x: 서쪽 통로 0~2 | 벽 3 | 화장실 4~19 | 벽 20 | 기계실 21~27 | 벽 28 | 동쪽 통로 29~30
    로컬 y: 천장 줄 0 | 화장실 1~3 | 바닥 4 | 샤워실 5~8 | 바닥 9"""
    T = lambda x, y, w, h, k='tile': d.tiles(ox + x, oy + y, w, h, k)
    T(3, 0, 26, 1); T(3, 4, 26, 1); T(3, 9, 26, 1)
    for x in (3, 20, 28):
        T(x, 1, 1, 3); T(x, 5, 1, 4)
    d.fill(ox + 0, oy + 0, 3, 10, '#24452e')
    d.ladder(ox + 1, oy + 0, 10)
    d.pole(ox + 2, oy + 0, 10)
    d.fill(ox + 29, oy + 0, 2, 10, '#2a2618')
    d.ladder(ox + 29, oy + 0, 10)
    d.pole(ox + 30, oy + 0, 10)
    dm = '' if zoom else None
    d.room(ox + 4, oy + 1, 16, 3, None if zoom else '화장실 (세척실)', 'wash', label_at='bottom',
           dims=dm if zoom else 'wh', dim_w_at=oy + .5, dim_h_at=ox + 3.5)
    d.room(ox + 21, oy + 1, 7, 3, '기계실', 'mech', label_at='bottom', dims='wh', dim_w_at=oy + 4.5, dim_h_at=ox + 28.5)
    d.room(ox + 4, oy + 5, 16, 4, None if zoom else '샤워실', 'wash', label_at='bottom',
           dims='' if zoom else 'wh', dim_w_at=oy + 9.5, dim_h_at=ox + 3.5)
    d.room(ox + 21, oy + 5, 7, 4, '여유', 'misc', label_at='top', dims='' if zoom else 'h', dim_h_at=ox + 28.5)
    for x in (4, 6, 16, 18):
        d.bld(ox + x, oy + 1, 2, 3, 'Sink', None, color='#9fe8ff', title='싱크대 2×3')
    for x in (8, 10, 12, 14):
        d.bld(ox + x, oy + 1, 2, 3, 'Lavatory', None, color='#ffffff', title='수세식 화장실 2×3')
    for x in range(4, 20, 2):
        d.bld(ox + x, oy + 5, 2, 4, 'Shower', None, color='#bfe6ff', title='샤워기 2×4')
    d.bld(ox + 21, oy + 1, 4, 3, 'Water_Sieve', '물 정화기 4×3' if zoom else None, color='#c0c8e0', title='물 정화기 4×3 · 120 W')
    d.bld(ox + 25, oy + 2, 1, 2, 'Storage_Bin', '모래' if zoom else None, color='#a9b0d0', title='저장 상자 (모래만, 우선순위 높게)')
    d.icon(ox + 26, oy + 1, 1, 3, 'Thimble_Reed', title='갈대')
    T(26, 4, 1, 1, 'hydro')
    for x in (3, 20, 28):
        d.door(ox + x, oy + 2)
    d.door(ox + 3, oy + 7)
    d.bld(ox + 21, oy + 0, 3, 1, 'Liquid_Bridge', None, color='#ffd34a', op=.6, title='액체 다리 3×1 (우선순위)')
    c = lambda x, y: (ox + x, oy + y)
    d.line([c(24, 3), c(4, 3), c(4, 8), c(19, 8)], 'liquid')
    d.line([c(5, 0), c(21, 0)], 'dirty')
    d.line([c(5, 5), c(20, 5), c(20, 0)], 'dirty')
    d.line([c(23, 0), c(23, 1)], 'dirty')
    d.line([c(21, 0), c(21, 1), c(27, 1), c(27, 4), c(26, 4)], 'o2', dash='5 3')


def wash_loop():
    d = BP('wash-loop', cols=31, rows=11, unit=22, x0=5, y0=1, show_zero=True,
           title='화장실·샤워실 폐쇄 루프 (샤워실이 화장실 바로 아래)', legend_cols=1,
           note='칸 번호 0~15 = 화장실 16칸, 16 = 벽(문), 17~23 = 기계실, 24 = 벽(문). 같은 번호를 기계실 확대 도면에서도 씁니다.')
    _wash(d, 0, 1)
    d.dim(0, 3, .5, '통로 3')
    d.key('line', '물: 정화기 → 싱크·수세식 8 → 서쪽 끝에서 아래로 → 샤워기 8, 마지막 샤워기에서 끝', 'liquid')
    d.key('line', '오염수: 출구마다 짧게 위로 빼서 천장 줄에 모음 (출구끼리 한 줄로 잇지 않기) → 액체 다리 → 물 정화기', 'dirty')
    d.key('dash', '넘침: 액체 다리 입구에서 가지 → 수경 재배 타일의 갈대 (다리 쪽이 먼저, 꽉 차면 갈대로)', 'o2')
    d.key('icon', '액체 다리 3×1 (천장 줄)', 'Liquid_Bridge')
    d.key('tile', '수경 재배 타일 (갈대 심는 칸, 바닥 줄)', 'hydro')
    return d


def machine_room():
    d = BP('machine-room', cols=13, rows=7, unit=44, x0=-13, y0=1, show_zero=True, rock=True,
           title='기계실 7×3 확대 (화장실 동쪽 옆)', legend_cols=1,
           note='17~20번: 물 정화기 · 21번: 모래 저장 상자(우선순위 높게) · 22번: 수경 재배 타일 위 갈대 · 23번: 지나다니는 칸\n'
                '문: 서쪽(16번) = 화장실, 동쪽(24번) = 동쪽 통로. 모래는 동쪽 통로로 들어옴.')
    # 로컬 x17 → 이 도면 x0 (화장실 끝 2칸 보이게)
    _wash(d, -18, 1, zoom=True)
    d.key('line', '물: 정화기 출력구 → 서쪽 벽을 지나 화장실 아래 줄', 'liquid')
    d.key('line', '오염수: 천장 줄(식당 바닥)로 와서 액체 다리 → 정화기 입력구', 'dirty')
    d.key('dash', '넘침: 다리 입구 칸에서 가지 → 23번 줄로 내려가 → 22번 수경 재배 타일', 'o2')
    return d


def build():
    return [corridor(), wash_loop(), machine_room()]
