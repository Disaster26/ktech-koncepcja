# Wektoryzacja rysunku technicznego K-Tech (PDF -> lekki SVG na tło pierwszego ekranu).
# Użycie: python rys_z_pdf.py plik.pdf x0 y0 x1 y1 wyjscie.svg
# Linie łączone w kilka ścieżek wg grubości, wypełnienia (groty) w jedną, napisy jako <text>.
import fitz, sys, math
src, x0, y0, x1, y1, out = sys.argv[1], *map(float, sys.argv[2:6]), sys.argv[6]
p = fitz.open(src)[0]
clip = fitz.Rect(x0, y0, x1, y1)
f = lambda v: ('%.1f' % v).rstrip('0').rstrip('.')
def pt(q): return f(q.x - x0) + ' ' + f(q.y - y0)
def path(d):
    s = ''; last = None
    for it in d['items']:
        k = it[0]
        if k == 'l':
            a, b = it[1], it[2]
            if last is None or abs(last.x - a.x) > .05 or abs(last.y - a.y) > .05: s += 'M' + pt(a)
            s += 'L' + pt(b); last = b
        elif k == 'c':
            a, b, c, e = it[1:5]
            if last is None or abs(last.x - a.x) > .05 or abs(last.y - a.y) > .05: s += 'M' + pt(a)
            s += 'C' + pt(b) + ' ' + pt(c) + ' ' + pt(e); last = e
        elif k == 're':
            r = it[1]; s += 'M' + pt(r.tl) + 'L' + pt(r.tr) + 'L' + pt(r.br) + 'L' + pt(r.bl) + 'Z'; last = None
        elif k == 'qu':
            q = it[1]; s += 'M' + pt(q.ul) + 'L' + pt(q.ur) + 'L' + pt(q.lr) + 'L' + pt(q.ll) + 'Z'; last = None
    if d.get('closePath'): s += 'Z'
    return s
strokes = {}; fills = []
for d in p.get_drawings():
    r = d['rect']
    if not clip.intersects(r) and not (r.width == 0 or r.height == 0) or not clip.contains(fitz.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)):
        continue
    t = d['type']
    if 'f' in t and d.get('fill') not in (None, (1.0, 1.0, 1.0)): fills.append(path(d))
    if 's' in t:
        w = d.get('width') or .3
        k = 'g' if w >= .45 else 'c'
        strokes.setdefault(k, []).append(path(d))
txt = []
for b in p.get_text('dict', clip=clip)['blocks']:
    for l in b.get('lines', []):
        cs, sn = l['dir']
        for s in l['spans']:
            t = s['text'].strip()
            if not t: continue
            o = s['origin']; fs = s['size']
            ang = math.degrees(math.atan2(sn, cs))
            tr = f' transform="rotate({f(ang)} {f(o[0]-x0)} {f(o[1]-y0)})"' if abs(ang) > .5 else ''
            t = t.replace('&', '&amp;').replace('<', '&lt;')
            txt.append(f'<text x="{f(o[0]-x0)}" y="{f(o[1]-y0)}" font-size="{f(fs)}"{tr}>{t}</text>')
W, H = x1 - x0, y1 - y0
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(W)} {f(H)}">'
       f'<g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">'
       + (f'<path stroke-width=".9" d="{"".join(strokes.get("g", []))}"/>' if strokes.get('g') else '')
       + (f'<path stroke-width=".35" d="{"".join(strokes.get("c", []))}"/>' if strokes.get('c') else '')
       + '</g>'
       + (f'<path fill="currentColor" d="{"".join(fills)}"/>' if fills else '')
       + f'<g fill="currentColor" font-family="Barlow,Arial,sans-serif">{"".join(txt)}</g></svg>')
open(out, 'w', encoding='utf-8', newline='\n').write(svg)
print(out, len(svg), 'B', 'linie', {k: len(v) for k, v in strokes.items()}, 'groty', len(fills), 'napisy', len(txt))
