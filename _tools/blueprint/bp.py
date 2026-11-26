"""타일 격자 도면 생성기.

모든 좌표는 타일 단위입니다. (x, y) = 왼쪽 위 칸, x는 오른쪽(동쪽), y는 아래쪽.
1칸 = 1타일 격자, 위·왼쪽 눈금(칸 번호), 치수선, 축척 막대, 인게임 아이콘을 그립니다.

출력은 `_includes/bp/<이름>.svg` 이고 페이지에서 `{% include bp/<이름>.svg %}` 로 넣습니다.
아이콘 경로는 Liquid(`{{ site.baseurl }}`)로 쓰기 때문에 Jekyll이 처리합니다.
미리보기용(`--preview`)은 아이콘을 로컬 파일 경로로 씁니다.
"""
from html import escape
import os

ICON_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'img', 'icons')

# 색 (기존 도면과 같은 계열)
C = dict(
    bg='#11131f', rock='#3a3128', ink='#e9ecf8', dim='#a9b0d0', faint='#6c7290',
    wall='#6b6e80', floor='#7a5a44', ins='#8a6a4a', door='#8fa3d8',
    water='#2c6d8c', polluted='#5a5a2a', brine='#3d6d6a',
    liquid='#5fb4ff', dirty='#d8913a', gas='#ff7ad9', o2='#7ad97a', h2='#ff7ad9', co2='#9b9b9b',
    wire='#ffe284', hwire='#e04848', auto='#7ad97a', heat='#ff8a5c', cold='#5fd0ff',
    envelope='#e8b04a', dimline='#ffd98a',
)

ROOM = dict(  # (채움, 테두리)
    bed=('#1f4a3a', '#7cf0c0'), barracks=('#2c4a2a', '#a3ff84'), food=('#4a4226', '#ffe284'),
    wash=('#20434a', '#84fff4'), research=('#3c2a48', '#d38be0'), farm=('#3b4720', '#cdf248'),
    ranch=('#4a3a24', '#e8c070'), ind=('#5a2a22', '#ff7a5c'), water=('#1d3358', '#6aa8ff'),
    misc=('#30344a', '#a9b0d0'), rec=('#1f3550', '#42a4f4'), med=('#4a2830', '#ff848e'),
    mech=('#4a3420', '#f4a442'), cool=('#173a48', '#5fd0ff'), plan=('#1c2036', '#6c7290'),
    gasroom=('#3a2f55', '#c9a0ff'),
)


class BP:
    def __init__(self, name, cols, rows, unit=20, title=None, x0=0, y0=0,
                 label_every=None, rock=True, note=None, legend_cols=2, top_pad=0, show_zero=False):
        self.name, self.cols, self.rows, self.u = name, cols, rows, unit
        self.title, self.note = title, note
        self.x0, self.y0 = x0, y0          # 이 칸이 1번 (눈금 번호 기준)
        self.every = label_every or (1 if cols <= 40 else 5)
        self.rock = rock
        self.nmin = 0 if show_zero else 1
        self.legend_cols = legend_cols
        self.ML = 30 if rows < 100 else 36
        self.MR = 16
        self.MT = (30 if title else 8) + 22 + top_pad
        self.layers = {k: [] for k in ('fill', 'tile', 'grid', 'bld', 'line', 'over', 'dim', 'label')}
        self.legend = []
        self.patterns = {}
        self.icons = set()
        self.extra_right = 0
        self.extra_bottom = 0
        self.open = set()   # 방·통로 칸 (autowalls 용)

    def mark_open(self, x, y, w, h):
        for i in range(int(round(x)), int(round(x + w))):
            for j in range(int(round(y)), int(round(y + h))):
                self.open.add((i, j))

    def autowalls(self, x, y, w, h, kind='tile', skip=()):
        """영역 안에서 방·통로 칸에 붙은(8방향) 칸을 벽·바닥 타일로 채움."""
        cells = set()
        for i in range(x, x + w):
            for j in range(y, y + h):
                if (i, j) in self.open or (i, j) in skip:
                    continue
                if any((i + a, j + b) in self.open for a in (-1, 0, 1) for b in (-1, 0, 1)):
                    cells.add((i, j))
        for j in range(y, y + h):
            i = x
            while i < x + w:
                if (i, j) in cells:
                    k = i
                    while (k, j) in cells:
                        k += 1
                    self.tiles(i, j, k - i, 1, kind)
                    i = k
                else:
                    i += 1

    # ---- 좌표 ----
    def X(self, x): return self.ML + x * self.u
    def Y(self, y): return self.MT + y * self.u

    def icon_href(self, icon):
        self.icons.add(icon)
        return '@@ICON:%s@@' % icon

    # ---- 채움 ----
    def fill(self, x, y, w, h, color, op=1, dash=False, stroke=None, layer='fill', open=False):
        if open:
            self.mark_open(x, y, w, h)
        s = ''
        if stroke:
            s = ' stroke="%s" stroke-width="1.5"%s' % (stroke, ' stroke-dasharray="4 3"' if dash else '')
        self.layers[layer].append('<rect x="%g" y="%g" width="%g" height="%g" fill="%s"%s%s/>' % (
            self.X(x), self.Y(y), w * self.u, h * self.u, color, '' if op == 1 else ' fill-opacity="%g"' % op, s))

    def tiles(self, x, y, w, h, kind='tile'):
        """타일 줄. kind = tile, ins(단열), farm, hydro, mesh, airflow, window, plastic, drywall."""
        icon = dict(tile='Tile', ins='Insulated_Tile', farm='Farm_Tile', hydro='Hydroponic_Farm',
                    mesh='Mesh_Tile', airflow='Airflow_Tile', window='Window_Tile',
                    plastic='Plastic_Tile', drywall='Drywall')[kind]
        pid = 'p-%s-%s' % (self.name, kind)
        if pid not in self.patterns:
            u = self.u
            self.patterns[pid] = (
                '<pattern id="%s" width="%g" height="%g" patternUnits="userSpaceOnUse" x="%g" y="%g">'
                '<rect width="%g" height="%g" fill="#4a4652"/>'
                '<image href="%s" x="-%g" y="-%g" width="%g" height="%g" preserveAspectRatio="none" opacity="%g"/></pattern>'
                % (pid, u, u, self.ML, self.MT, u, u, self.icon_href(icon), u * .06, u * .02, u * 1.12, u * 1.1,
                   1 if u >= 16 else .55))
        self.layers['tile'].append('<rect x="%g" y="%g" width="%g" height="%g" fill="url(#%s)"/>' % (
            self.X(x), self.Y(y), w * self.u, h * self.u, pid))

    def room(self, x, y, w, h, name=None, kind='misc', dims='wh', sub=None, label_at='top',
             dashed=False, fill=None, dim_w_at=None, dim_h_at=None, label_size=None, size_in_label=True):
        """방 내부(벽 제외). dims: 'w' 가로 치수선(방 바로 위 벽 줄), 'h' 세로 치수선(방 바로 왼쪽 벽 줄)."""
        f, s = ROOM[kind]
        if not dashed:
            self.mark_open(x, y, w, h)
        if fill:
            f = fill
        self.fill(x, y, w, h, f, op=.55 if dashed else 1)
        self.layers['over'].append(
            '<rect x="%g" y="%g" width="%g" height="%g" fill="none" stroke="%s" stroke-width="%g"%s/>' % (
                self.X(x) + .75, self.Y(y) + .75, w * self.u - 1.5, h * self.u - 1.5, s,
                1.5, ' stroke-dasharray="5 3" stroke-opacity=".8"' if dashed else ''))
        if name:
            fs = label_size or max(8.5, min(12, self.u * .62))
            txt = name + ((' %d×%d' % (w, h)) if size_in_label else '')
            if label_at == 'top':
                ly = self.Y(y) + fs + 2
            elif label_at == 'mid':
                ly = self.Y(y) + h * self.u / 2 + fs / 3
            else:
                ly = self.Y(y + h) - 4
            self.text(self.X(x) + w * self.u / 2, ly, txt, s, fs, bold=True, halo=True, raw=True)
            if sub:
                self.text(self.X(x) + w * self.u / 2, ly + fs + 1, sub, C['ink'], fs * .78, halo=True, raw=True)
        if 'w' in dims:
            yy = y - .5 if dim_w_at is None else dim_w_at
            self.dim(x, x + w, yy)
        if 'h' in dims:
            xx = x - .5 if dim_h_at is None else dim_h_at
            self.vdim(xx, y, y + h)

    def envelope(self, x, y, w, h, label=None):
        self.layers['over'].append(
            '<rect x="%g" y="%g" width="%g" height="%g" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="9 5"/>'
            % (self.X(x), self.Y(y), w * self.u, h * self.u, C['envelope']))

    # ---- 건물 ----
    def bld(self, x, y, w, h, icon=None, label=None, color='#c0c8e0', planned=False, op=.28, title=None,
            label_pos='in', fs=None, icon_scale=1.0):
        X, Y, W, H = self.X(x), self.Y(y), w * self.u, h * self.u
        a = ' opacity=".55"' if planned else ''
        g = ['<g%s>' % a]
        if title or label:
            g.append('<title>%s</title>' % escape(title or label))
        g.append('<rect x="%g" y="%g" width="%g" height="%g" rx="2" fill="%s" fill-opacity="%g" stroke="%s" stroke-width="1.2"%s/>' % (
            X + 1, Y + 1, W - 2, H - 2, color, op, color, ' stroke-dasharray="4 3"' if planned else ''))
        if icon:
            pad = max(1.0, self.u * .06)
            iw, ih = (W - 2 * pad) * icon_scale, (H - 2 * pad) * icon_scale
            g.append('<image href="%s" x="%g" y="%g" width="%g" height="%g" preserveAspectRatio="xMidYMax meet"/>' % (
                self.icon_href(icon), X + (W - iw) / 2, Y + H - pad - ih, iw, ih))
        g.append('</g>')
        self.layers['bld'].append(''.join(g))
        if label and label_pos != 'none':
            fs = fs or max(7.5, min(10, self.u * .45))
            if label_pos == 'in':
                self.text(X + W / 2, Y + fs + 1, label, C['ink'], fs, bold=True, halo=True, raw=True)
            elif label_pos == 'below':
                self.text(X + W / 2, Y + H + fs + 1, label, C['ink'], fs, halo=True, raw=True)
            elif label_pos == 'above':
                self.text(X + W / 2, Y - 3, label, C['ink'], fs, halo=True, raw=True)

    def icon(self, x, y, w, h, icon, title=None, op=1):
        X, Y, W, H = self.X(x), self.Y(y), w * self.u, h * self.u
        t = '<title>%s</title>' % escape(title) if title else ''
        self.layers['bld'].append('<g%s>%s<image href="%s" x="%g" y="%g" width="%g" height="%g" preserveAspectRatio="xMidYMax meet"/></g>' % (
            '' if op == 1 else ' opacity="%g"' % op, t, self.icon_href(icon), X, Y, W, H))

    def plants(self, x, y, n, icon='Mealwood', step=1, h=2, title=None):
        """작물 n그루. (x, y) = 첫 작물 아래칸(심은 타일 바로 위 칸)의 왼쪽 위. 작물은 위로 h칸."""
        for i in range(n):
            self.icon(x + i * step, y - h + 1, 1, h, icon, title=title)

    def ladder(self, x, y, h, kind='Ladder'):
        self.mark_open(x, y, 1, h)
        pid = 'p-%s-%s' % (self.name, kind)
        if pid not in self.patterns:
            u = self.u
            self.patterns[pid] = (
                '<pattern id="%s" width="%g" height="%g" patternUnits="userSpaceOnUse" x="%g" y="%g">'
                '<image href="%s" width="%g" height="%g" preserveAspectRatio="xMidYMid meet"/></pattern>'
                % (pid, u, u, self.ML, self.MT, self.icon_href(kind), u, u))
        self.layers['bld'].append('<rect x="%g" y="%g" width="%g" height="%g" fill="url(#%s)"/>' % (
            self.X(x), self.Y(y), self.u, h * self.u, pid))

    def pole(self, x, y, h):
        self.ladder(x, y, h, 'Fire_Pole')

    def door(self, x, y, w=1, h=2, kind='Pneumatic_Door', color=None):
        self.bld(x, y, w, h, kind, color=color or C['door'], op=.35, title='문 (%s)' % kind.replace('_', ' '))

    # ---- 선 ----
    def line(self, pts, kind='liquid', w=None, dash=None, label=None, arrow=False, center=True):
        col = C.get(kind, kind)
        width = w or max(2.5, self.u * .16)
        off = .5 if center else 0
        d = 'M' + ' L'.join('%g %g' % (self.X(px + off), self.Y(py + off)) for px, py in pts)
        extra = ''
        if dash:
            extra += ' stroke-dasharray="%s"' % dash
        if arrow:
            extra += ' marker-end="url(#arr-%s)"' % self.name
        if kind in ('ins_liquid', 'ins_cold', 'ins_hot'):
            col = dict(ins_liquid=C['liquid'], ins_cold=C['cold'], ins_hot=C['heat'])[kind]
            self.layers['line'].append('<path d="%s" fill="none" stroke="#f0e6c8" stroke-width="%g" stroke-linejoin="round" stroke-opacity=".8"/>' % (d, width + 3))
        self.layers['line'].append('<path d="%s" fill="none" stroke="%s" stroke-width="%g" stroke-linejoin="round" stroke-linecap="round"%s/>' % (d, col, width, extra))

    # ---- 치수선 ----
    def dim(self, x1, x2, y, text=None, color=None):
        """가로 치수선: 타일 경계 x1~x2, 높이 y(타일 좌표, 보통 벽 줄 가운데 = 정수+.5)."""
        col = color or C['dimline']
        X1, X2, Yy = self.X(x1), self.X(x2), self.Y(y)
        n = text if text is not None else '%g' % (x2 - x1)
        t = 3.5
        self.layers['dim'].append(
            '<g class="dim"><path d="M%g %g v%g M%g %g v%g M%g %g H%g" stroke="%s" stroke-width="1" fill="none"/>'
            '<path d="M%g %g l5 -2.5 v5 z M%g %g l-5 -2.5 v5 z" fill="%s"/></g>' % (
                X1, Yy - t, 2 * t, X2, Yy - t, 2 * t, X1 + 1, Yy, X2 - 1, col,
                X1 + .5, Yy, X2 - .5, Yy, col))
        self.pill(Yy, (X1 + X2) / 2, str(n), col)

    def vdim(self, x, y1, y2, text=None, color=None):
        col = color or C['dimline']
        Xx, Y1, Y2 = self.X(x), self.Y(y1), self.Y(y2)
        n = text if text is not None else '%g' % (y2 - y1)
        t = 3.5
        self.layers['dim'].append(
            '<g class="dim"><path d="M%g %g h%g M%g %g h%g M%g %g V%g" stroke="%s" stroke-width="1" fill="none"/>'
            '<path d="M%g %g l-2.5 5 h5 z M%g %g l-2.5 -5 h5 z" fill="%s"/></g>' % (
                Xx - t, Y1, 2 * t, Xx - t, Y2, 2 * t, Xx, Y1 + 1, Y2 - 1, col,
                Xx, Y1 + .5, Xx, Y2 - .5, col))
        self.pill((Y1 + Y2) / 2, Xx, str(n), col)

    def pill(self, cy, cx, s, col):
        fs = 9 if self.u >= 14 else 8
        w = len(s) * fs * .62 + 5
        self.layers['dim'].append(
            '<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="#11131f" stroke="%s" stroke-width=".8"/>'
            '<text x="%g" y="%g" fill="%s" font-size="%g" text-anchor="middle" font-weight="700">%s</text>' % (
                cx - w / 2, cy - fs / 2 - 1.5, w, fs + 3, col, cx, cy + fs * .36, col, fs, escape(s)))

    # ---- 글자 ----
    def text(self, x, y, s, color=None, size=10, anchor='middle', bold=False, halo=False, raw=False, layer='label'):
        X = x if raw else self.X(x)
        Y = y if raw else self.Y(y)
        h = ' paint-order="stroke" stroke="#11131f" stroke-width="3" stroke-linejoin="round"' if halo else ''
        self.layers[layer].append('<text x="%g" y="%g" fill="%s" font-size="%g" text-anchor="%s"%s%s>%s</text>' % (
            X, Y, color or C['ink'], size, anchor, ' font-weight="700"' if bold else '', h, escape(s)))

    def note_at(self, x, y, s, color=None, size=10, anchor='start'):
        self.text(x, y, s, color or C['dim'], size, anchor=anchor, halo=True)

    # ---- 범례 ----
    def key(self, kind, text, val=None):
        """kind: 'fill'(색), 'line'(색), 'dash'(색), 'icon'(아이콘 이름), 'tile'(타일 종류), 'env'."""
        self.legend.append((kind, val, text))

    # ---- 출력 ----
    def _grid(self):
        u, cols, rows = self.u, self.cols, self.rows
        x0, y0, x1, y1 = self.X(0), self.Y(0), self.X(cols), self.Y(rows)
        minor = ''.join('M%g %gV%g' % (self.X(i), y0, y1) for i in range(cols + 1) if (i - self.x0) % 5) + \
            ''.join('M%g %gH%g' % (x0, self.Y(j), x1) for j in range(rows + 1) if (j - self.y0) % 5)
        major = ''.join('M%g %gV%g' % (self.X(i), y0, y1) for i in range(cols + 1) if not (i - self.x0) % 5) + \
            ''.join('M%g %gH%g' % (x0, self.Y(j), x1) for j in range(rows + 1) if not (j - self.y0) % 5)
        out = ['<path d="%s" stroke="#ffffff" stroke-opacity=".09" stroke-width="1" fill="none"/>' % minor,
               '<path d="%s" stroke="#ffffff" stroke-opacity=".24" stroke-width="1" fill="none"/>' % major]
        # 눈금
        tk = []
        for i in range(cols):
            n = i - self.x0 + 1
            cx = self.X(i) + u / 2
            big = n % 5 == 0 or n == 1
            tk.append('M%g %gv%g' % (cx, y0 - 2, -(5 if big else 3)))
            if n >= self.nmin and (n % self.every == 0 or n == 1 or self.every == 1):
                out.append('<text x="%g" y="%g" fill="%s" font-size="%g" text-anchor="middle">%d</text>' % (
                    cx, y0 - 9, '#cfd3e6' if big else '#8a90ad', 8.5 if u < 16 else 9, n))
        for j in range(rows):
            n = j - self.y0 + 1
            cy = self.Y(j) + u / 2
            big = n % 5 == 0 or n == 1
            tk.append('M%g %gh%g' % (x0 - 2, cy, -(5 if big else 3)))
            if n >= self.nmin and (n % self.every == 0 or n == 1 or self.every == 1):
                out.append('<text x="%g" y="%g" fill="%s" font-size="%g" text-anchor="end">%d</text>' % (
                    x0 - 9, cy + 3, '#cfd3e6' if big else '#8a90ad', 8.5 if u < 16 else 9, n))
        out.append('<path d="%s" stroke="#8a90ad" stroke-width="1"/>' % ''.join(tk))
        return out

    def _legend(self, top):
        out = []
        W = self.X(self.cols) + self.extra_right
        colw = (W - 20) / self.legend_cols
        y = top
        # 축척 막대
        u = self.u
        n = 5 if u >= 14 else 10
        bx = 20
        out.append('<text x="%g" y="%g" fill="%s" font-size="11" font-weight="700">축척</text>' % (bx, y + 11, C['ink']))
        bx += 34
        for i in range(n):
            out.append('<rect x="%g" y="%g" width="%g" height="8" fill="%s" stroke="#cfd3e6" stroke-width=".8"/>' % (
                bx + i * u, y + 3, u, '#cfd3e6' if i % 2 == 0 else '#11131f'))
        out.append('<text x="%g" y="%g" fill="%s" font-size="10">%d칸</text>' % (bx + n * u + 5, y + 11, C['dim'], n))
        info = '1칸 = 1타일 · 전체 %d × %d칸 · 눈금 숫자 = 칸 번호, 굵은 선 5칸마다' % (self.cols, self.rows)
        if W < 760:
            out.append('<text x="20" y="%g" fill="%s" font-size="10">%s</text>' % (y + 28, C['dim'], escape(info)))
            y += 18
        else:
            out.append('<text x="%g" y="%g" fill="%s" font-size="10">%s</text>' % (bx + n * u + 38, y + 11, C['dim'], escape(info)))
        y += 24
        for i, (kind, val, text) in enumerate(self.legend):
            cx = 20 + (i % self.legend_cols) * colw
            cy = y + (i // self.legend_cols) * 20
            sw = ''
            if kind == 'fill':
                sw = '<rect x="%g" y="%g" width="16" height="12" rx="2" fill="%s"/>' % (cx, cy, val)
            elif kind == 'room':
                f, s = ROOM[val]
                sw = '<rect x="%g" y="%g" width="16" height="12" rx="2" fill="%s" stroke="%s" stroke-width="1.5"/>' % (cx, cy, f, s)
            elif kind == 'line':
                sw = '<path d="M%g %g h16" stroke="%s" stroke-width="3.5"/>' % (cx, cy + 6, C.get(val, val))
            elif kind == 'dash':
                sw = '<path d="M%g %g h16" stroke="%s" stroke-width="3" stroke-dasharray="4 2"/>' % (cx, cy + 6, C.get(val, val))
            elif kind == 'ins':
                sw = ('<path d="M%g %g h16" stroke="#f0e6c8" stroke-width="6" stroke-opacity=".8"/>'
                      '<path d="M%g %g h16" stroke="%s" stroke-width="3"/>') % (cx, cy + 6, cx, cy + 6, C.get(val, val))
            elif kind == 'env':
                sw = '<path d="M%g %g h16" stroke="%s" stroke-width="3" stroke-dasharray="6 3"/>' % (cx, cy + 6, C['envelope'])
            elif kind == 'dim':
                sw = '<path d="M%g %g h16 M%g %g v6 M%g %g v6" stroke="%s" stroke-width="1"/>' % (
                    cx, cy + 6, cx, cy + 3, cx + 16, cy + 3, C['dimline'])
            elif kind == 'icon':
                sw = '<image href="%s" x="%g" y="%g" width="18" height="16" preserveAspectRatio="xMidYMid meet"/>' % (
                    self.icon_href(val), cx - 1, cy - 2)
            elif kind == 'tile':
                icon = dict(tile='Tile', ins='Insulated_Tile', farm='Farm_Tile', hydro='Hydroponic_Farm',
                            mesh='Mesh_Tile', airflow='Airflow_Tile', window='Window_Tile',
                            plastic='Plastic_Tile', drywall='Drywall')[val]
                sw = '<image href="%s" x="%g" y="%g" width="16" height="14" preserveAspectRatio="none"/>' % (
                    self.icon_href(icon), cx, cy - 1)
            out.append(sw + '<text x="%g" y="%g" fill="%s" font-size="10.5">%s</text>' % (cx + 24, cy + 10, C['ink'], escape(text)))
        rows = (len(self.legend) + self.legend_cols - 1) // self.legend_cols
        y += rows * 20 + 6
        if self.note:
            for ln in self.note.split('\n'):
                out.append('<text x="20" y="%g" fill="%s" font-size="10">%s</text>' % (y + 8, C['dim'], escape(ln)))
                y += 15
        out.append('<text x="20" y="%g" fill="%s" font-size="9">건물·타일 아이콘 © Klei Entertainment · 비공식 팬 가이드</text>' % (y + 10, C['faint']))
        y += 18
        return out, y

    def svg(self, icon_base):
        W = self.X(self.cols) + self.MR + self.extra_right
        top = self.Y(self.rows) + 14 + self.extra_bottom
        leg, H = self._legend(top)
        H += 6
        head = []
        if self.title:
            head.append('<text x="20" y="22" fill="%s" font-size="14" font-weight="700">%s</text>' % (C['ink'], escape(self.title)))
        defs = ['<marker id="arr-%s" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker>' % self.name]
        defs += list(self.patterns.values())
        body = ['<rect width="%g" height="%g" fill="%s"/>' % (W, H, C['bg'])]
        if self.rock:
            body.append('<rect x="%g" y="%g" width="%g" height="%g" fill="%s"/>' % (
                self.X(0), self.Y(0), self.cols * self.u, self.rows * self.u, C['rock']))
        defs.append('<clipPath id="clip-%s"><rect x="%g" y="%g" width="%g" height="%g"/></clipPath>' % (
            self.name, self.X(0), self.Y(0), self.cols * self.u, self.rows * self.u))
        body.append('<g clip-path="url(#clip-%s)">' % self.name)
        body += self.layers['fill'] + self.layers['tile']
        body.append('</g>')
        body += self._grid()
        body.append('<g clip-path="url(#clip-%s)">' % self.name)
        body += self.layers['bld'] + self.layers['line'] + self.layers['over']
        body.append('</g>')
        body += self.layers['dim'] + self.layers['label']
        aria = self.title or self.name
        s = ('<svg viewBox="0 0 %g %g" width="%g" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg" '
             'font-family="Noto Sans KR, sans-serif" class="bp-svg" style="min-width:%gpx;max-width:%gpx"><defs>%s</defs>%s%s%s</svg>' % (
                 W, H, W, escape(aria), min(W, 680), W, ''.join(defs), ''.join(body), ''.join(head), ''.join(leg)))
        import re
        return re.sub(r'@@ICON:([^@]+)@@', lambda m: icon_base + m.group(1) + '.png', s), W
