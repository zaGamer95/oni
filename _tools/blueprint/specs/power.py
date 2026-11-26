from bp import BP, C


def _shell(d, oy):
    d.fill(0, oy, 3, 6, '#24452e')
    d.ladder(1, oy, 6)
    d.pole(2, oy, 6)
    d.tiles(3, oy, 26, 1, 'ins')      # 천장 = 단열 격벽 줄
    d.tiles(3, oy + 5, 26, 1)
    d.tiles(3, oy + 1, 1, 4)
    d.tiles(28, oy + 1, 1, 4)
    d.door(3, oy + 3)


def early():
    d = BP('power-early', cols=30, rows=7, unit=24, x0=4, y0=1,
           title='초반 (사이클 10~30): 발전소 24×4, 석탄 발전기 1대부터', legend_cols=2,
           note='6~8번 석탄 발전기 · 9번 석탄 저장 상자 · 18~19번 배터리 2개 · 점선 자리는 비워 둠. 천장 줄 = 단열 격벽(이 방은 격벽 밖).')
    oy = 1
    _shell(d, oy)
    d.room(4, oy + 1, 24, 4, '발전소', 'ind', dims='wh', label_at='top', dim_w_at=oy + 5.5)
    B = lambda x, w, h, icon, lab, col, plan=False, t=None: d.bld(x + 3, oy + 5 - h, w, h, icon, lab, color=col, planned=plan, title=t)
    B(1, 2, 2, 'Power_Transformer', '변압', '#ffe284', True, '변압기 2×2 (나중)')
    B(3, 2, 2, 'Power_Transformer', '변압', '#ffe284', True, '변압기 2×2 (나중)')
    B(6, 3, 3, 'Coal_Generator', '석탄 발전기', '#ff7a5c', t='석탄 발전기 3×3 · 600 W')
    B(9, 1, 2, 'Storage_Bin', None, '#a9b0d0', t='석탄 저장 상자 1×2')
    B(10, 3, 3, 'Coal_Generator', '2호기', '#ff7a5c', True, '석탄 발전기 2호기 (나중)')
    B(18, 1, 2, 'Battery', None, '#8fe3ff', t='배터리 1×2')
    B(19, 1, 2, 'Battery', None, '#8fe3ff', t='배터리 1×2')
    B(20, 2, 2, 'Smart_Battery', '스마트', '#5fd0ff', True, '스마트 배터리 2×2 (나중)')
    B(23, 2, 4, 'Power_Control_Station', '제어소', '#e0a0ff', True, '전력 제어소 2×4 (나중)')
    d.line([(10, oy + 2), (10, oy + 1), (21.6, oy + 1), (21.6, oy + 3)], 'wire')
    d.line([(1.4, oy + 1), (10, oy + 1)], 'wire')
    d.key('line', '일반 와이어 (1 kW) 한 회로', 'wire')
    d.key('fill', '점선 = 나중에 놓을 자리', '#3a3d55')
    d.key('tile', '천장 = 단열 타일 (격벽 줄)', 'ins')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def mid():
    d = BP('power-mid', cols=30, rows=7, unit=24, x0=4, y0=1,
           title='중반 (사이클 40~): 석탄 3대 + 스마트 배터리 자동화 + 헤비와트 + 변압기', legend_cols=2,
           note='1~4번 변압기 2개 · 6~8, 10~12, 14~16번 석탄 발전기 · 9, 13번 석탄 저장 상자 · 18~21번 스마트 배터리 2개 · 23~24번 전력 제어소.')
    oy = 1
    _shell(d, oy)
    d.room(4, oy + 1, 24, 4, '발전소', 'ind', dims='wh', label_at='top', dim_w_at=oy + 5.5)
    B = lambda x, w, h, icon, lab, col, t=None: d.bld(x + 3, oy + 5 - h, w, h, icon, lab, color=col, title=t)
    B(1, 2, 2, 'Power_Transformer', '변압 1', '#ffe284', '변압기 2×2 (위 입력, 아래 출력)')
    B(3, 2, 2, 'Power_Transformer', '변압 2', '#ffe284', '변압기 2×2')
    for i, x in enumerate((6, 10, 14)):
        B(x, 3, 3, 'Coal_Generator', '석탄 %d' % (i + 1), '#ff7a5c', '석탄 발전기 3×3 · 600 W')
    B(9, 1, 2, 'Storage_Bin', None, '#a9b0d0', '석탄 저장 상자 1×2')
    B(13, 1, 2, 'Storage_Bin', None, '#a9b0d0', '석탄 저장 상자 1×2')
    B(18, 2, 2, 'Smart_Battery', '스마트', '#5fd0ff', '스마트 배터리 2×2')
    B(20, 2, 2, 'Smart_Battery', '스마트', '#5fd0ff', '스마트 배터리 2×2')
    B(23, 2, 4, 'Power_Control_Station', '제어소', '#e0a0ff', '전력 제어소 2×4')
    d.line([(5.5, oy + 1), (24.5, oy + 1)], 'hwire', w=6)
    d.line([(4.5, oy + 3), (4.5, oy + 1.6), (1.4, oy + 1.6)], 'wire')
    d.line([(6.5, oy + 3), (6.5, oy + 2.2), (1.4, oy + 2.2)], 'wire')
    d.line([(10, oy + 4.4), (21.5, oy + 4.4)], 'auto', w=2.5, dash='5 3')
    d.key('line', '헤비와트 와이어 (20 kW, 발전소 안에서만)', 'hwire')
    d.key('line', '변압기마다 일반 와이어 (1 kW) 회로 하나씩 통로로', 'wire')
    d.key('dash', '자동화 와이어: 스마트 배터리 50% 이하 켜기, 90% 이상 끄기', 'auto')
    d.key('dim', '치수선 (방 안쪽 칸 수)')
    return d


def build():
    return [early(), mid()]
