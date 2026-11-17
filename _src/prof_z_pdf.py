import fitz, sys, json
p=fitz.open(sys.argv[1])[0]
W=p.get_text('words')
syms=[(w[1],w[4]) for w in W if 180<w[0]<230 and w[4]!='Symbol']
syms.sort()
D=[d for d in p.get_drawings() if d['rect'].x1<185 and d['rect'].y0>100]
def col(c):
    if c is None: return 'none'
    return '#%02X%02X%02X'%tuple(round(x*255) for x in c)
def path(d):
    s=''; last=None
    for it in d['items']:
        k=it[0]
        if k=='l':
            a,b=it[1],it[2]
            if last is None or abs(last.x-a.x)>.01 or abs(last.y-a.y)>.01: s+='M%.2f %.2f'%(a.x,a.y)
            s+='L%.2f %.2f'%(b.x,b.y); last=b
        elif k=='c':
            a,b,c,e=it[1:5]
            if last is None or abs(last.x-a.x)>.01 or abs(last.y-a.y)>.01: s+='M%.2f %.2f'%(a.x,a.y)
            s+='C%.2f %.2f %.2f %.2f %.2f %.2f'%(b.x,b.y,c.x,c.y,e.x,e.y); last=e
        elif k=='re':
            r=it[1]; s+='M%.2f %.2fH%.2fV%.2fH%.2fZ'%(r.x0,r.y0,r.x1,r.y1,r.x0); last=None
        elif k=='qu':
            q=it[1]; s+='M'+'L'.join('%.2f %.2f'%(pt.x,pt.y) for pt in (q.ul,q.ur,q.lr,q.ll))+'Z'; last=None
    if d.get('closePath'): s+='Z'
    return s
out={}
for i,(y,name) in enumerate(syms):
    y0=y-4; y1=syms[i+1][0]-4 if i+1<len(syms) else 760
    ds=[d for d in D if y0<=(d['rect'].y0+d['rect'].y1)/2<y1]
    if not ds: continue
    r=fitz.Rect(min(d['rect'].x0 for d in ds),min(d['rect'].y0 for d in ds),max(d['rect'].x1 for d in ds),max(d['rect'].y1 for d in ds))
    els=[]
    for d in ds:
        t=d['type']; f=col(d.get('fill')) if 'f' in t else 'none'; st=col(d.get('color')) if 's' in t else 'none'
        a=f'<path d="{path(d)}" fill="{f}"'
        if d.get('even_odd') and f!='none': a+=' fill-rule="evenodd"'
        if st!='none':
            w=max(d.get('width') or .3,.3); a+=f' stroke="{st}" stroke-width="{w:.2f}"'
            if d.get('lineJoin'): a+=' stroke-linejoin="round"'
        if (d.get('fill_opacity') or 1)<1: a+=f' fill-opacity="{d["fill_opacity"]:.2f}"'
        els.append(a+'/>')
    pad=1
    vb=f'{r.x0-pad:.2f} {r.y0-pad:.2f} {r.width+2*pad:.2f} {r.height+2*pad:.2f}'
    key=name.lower() if name not in out else name.lower()+'2'
    while key in out: key+='x'
    out[key]={'sym':name,'vb':vb,'w':r.width,'h':r.height,'body':''.join(els)}
    print(key, name, vb, len(ds), file=sys.stderr)
json.dump(out,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False)
