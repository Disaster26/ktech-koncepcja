# Treść działu Uszczelnienia techniczne: lista profili wg SPIS i karty modeli.
import os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from karty_dane import KARTY, SPIS

esc = lambda s: html.escape(s, quote=True)
ZIEL = '#2E8B57'; KR = '#2B2F34'
HATCH = '<defs><pattern id="hx{n}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#6B7178" stroke-width=".8"/></pattern></defs>'
LINIE = '<path d="M38 8H98M38 28H98M38 48H98" stroke="#9AA1A9" stroke-width="1" fill="none"/>'
def g(d, fill=ZIEL): return f'<path d="{d}" fill="{fill}" stroke="{KR}" stroke-width="1.2" stroke-linejoin="round"/>'
def wb(x, y, w=6, h=5): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="{KR}" stroke-width="1"/>'
RAMKA = '<path d="M10 6H98M10 50H98" stroke="#9AA1A9" stroke-width="1"/>'
def hrect(n, x, y, w, h): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#hx{n})" stroke="{KR}" stroke-width="1.2"/>'
PROF = {
  'ds':  lambda n: LINIE + g('M14 4H32V52H14L10 46L14 40L10 34L14 28L10 22L14 16L10 10Z') + wb(14, 4) + wb(14, 47),
  'dsn': lambda n: LINIE + g('M20 4H30Q34 4 34 10V46Q34 52 30 52H20Z', KR) + g('M20 10V46H14L10 38V18L14 10Z') + wb(14, 4, 8) + wb(14, 47, 8),
  'dz':  lambda n: LINIE + g('M12 10H34V50H12L9 42V18Z') + wb(12, 10, 7) + wb(12, 45, 7),
  'po':  lambda n: HATCH.format(n=n) + LINIE + hrect(n, 10, 22, 26, 12),
  'pp':  lambda n: HATCH.format(n=n) + RAMKA + hrect(n, 10, 6, 7, 44) + '<path d="M60 6V50" stroke="#9AA1A9"/>',
  'wfe': lambda n: HATCH.format(n=n) + RAMKA + hrect(n, 10, 6, 7, 44) + '<path d="M60 6V50M44 50 78 6" stroke="#9AA1A9"/>',
  'jsn': lambda n: LINIE + g('M10 8H30V16L35 22V40L28 48H14L10 42Z') + f'<circle cx="16" cy="40" r="6" fill="{KR}"/>' + wb(30, 6, 5, 5),
  'js':  lambda n: LINIE + g('M10 10H30V18L35 22V40L27 48L23 42H15L11 48L10 40Z') + wb(30, 8, 5, 5),
  'pz':  lambda n: LINIE + g('M14 22H28L35 8L37 11L31 24V44H14Z'),
  'pw':  lambda n: HATCH.format(n=n) + RAMKA + f'<path d="M14 6H20V50H14V36H10V20H14Z" fill="url(#hx{n})" stroke="{KR}" stroke-width="1.2"/>' + '<path d="M60 6V50M44 50 78 6" stroke="#9AA1A9"/>',
  'pe':  lambda n: HATCH.format(n=n) + LINIE + f'<path d="M10 24Q24 30 38 24V34H10Z" fill="url(#hx{n})" stroke="{KR}" stroke-width="1.2"/>',
  'o':   lambda n: LINIE + '<circle cx="22" cy="28" r="10" fill="#3B4148"/>',
  'vk':  lambda n: LINIE + g('M14 14H24V30L28 42L24 44L20 34L17 44L12 42L14 30Z'),
  'du':  lambda n: LINIE + g('M13 14H29L33 21L29 28L33 35L29 42H13L9 35L13 28L9 21Z', '#C4C8CC'),
}
def profil(key, n):
    return f'<svg class="prof" viewBox="0 0 100 56" aria-hidden="true" focusable="false">{PROF[key](n)}</svg>'

KARTA = {k['slug']: k for k in KARTY}

def lista():
    el = []
    for i, (sym, typ, mat, slug, pk) in enumerate(SPIS):
        txt = f'<span class="mod-txt"><b>{esc(sym)}</b><span>{esc(typ)}</span><span class="mod-mat">Materiał: {esc(mat)}</span>'
        if slug:
            n = len(KARTA[slug]['rows'])
            el.append(f'<li class="mod mod-gotowy"><a href="{slug}/">{profil(pk, i)}{txt}<em>Karta i wymiary ({n} rozmiarów)</em></span></a></li>')
        else:
            el.append(f'<li class="mod"><div>{profil(pk, i)}{txt}<em class="mod-wkrotce">Karta w przygotowaniu</em></span></div></li>')
    return '\n        '.join(el)

def dzial():
    return f'''
<section class="sekcja pod-glowa">
  <div class="wrap">
    <nav class="okruchy" aria-label="Jesteś tutaj"><a href="../">Strona główna</a><span>/</span><a href="../#oferta">Oferta</a><span>/</span><span aria-current="page">Uszczelnienia techniczne</span></nav>
    <div class="pod-wstep">
      <div>
        <h1><i class="znak" aria-hidden="true"></i>Uszczelnienia techniczne</h1>
        <p>Uszczelnienia do hydrauliki siłowej, w większości do siłowników górniczych. Każdy model ma kartę z parametrami pracy oraz tabelą wymiarów uszczelki i gniazda. Gdy potrzebnego rozmiaru nie ma w tabeli, prosimy o zapytanie z wymiarami gniazda.</p>
        <p class="pod-kontakt"><a href="tel:+48663005555">663 005 555</a><a href="mailto:biuro@k-tech.net.pl">biuro@k-tech.net.pl</a></p>
      </div>
      <figure class="pod-profil"><img src="../img/u/dsn-zabudowa.webp" alt="Uszczelnienie DSn w gnieździe tłoka - rysunek zabudowy" width="764" height="459" fetchpriority="high"><figcaption>DSn w gnieździe tłoka, karta KT-DSn01</figcaption></figure>
    </div>
  </div>
</section>

<section class="sekcja mod-sekcja">
  <div class="wrap">
    <h2 class="mod-tyt">Podstawowe profile</h2>
    <ul class="mod-lista">
        {lista()}
    </ul>
    <p class="mod-nota">Kolejne modele i rozmiary można dodawać samodzielnie w panelu strony.</p>
  </div>
</section>
'''

def num(v):
    return re.sub(r'^\(.*?\)', '', v)

def tabela(k):
    kol = k['kol']; usz = k['usz']; iD3 = [s for s, _ in kol].index('D3')
    rows = []
    for c in k['rows']:
        assert len(c) == len(kol), (k['slug'], c)
        ozn = k['sym'] + ' ' + ' x '.join(num(v) for v in c[:usz])
        td = ''.join(('<td class="zab">' if j >= usz else '<td>') + esc(v) + '</td>' for j, v in enumerate(c))
        rows.append(f'<tr data-d1="{c[0]}" data-d2="{c[1]}" data-d3="{c[iD3]}"><th scope="row">{esc(ozn)}</th>{td}</tr>')
    th2 = ''.join(('<th scope="col" class="zab">' if j >= usz else '<th scope="col">') + f'<b>{s}</b><span>{esc(o)}</span></th>' for j, (s, o) in enumerate(kol))
    grupa = 'Pierścień' if k['slug'] in ('po', 'pz') else 'Uszczelka'
    return f'''<table id="tab-wym" class="tab-wym u{usz}">
        <thead>
          <tr class="tab-grupy"><th scope="col" rowspan="2" class="tab-ozn">Oznaczenie</th><th colspan="{usz}" scope="colgroup">{grupa}</th><th colspan="{len(kol) - usz}" scope="colgroup" class="zab">Gniazdo (zabudowa)</th></tr>
          <tr>{th2}</tr>
        </thead>
        <tbody>
          {chr(10).join(rows)}
        </tbody>
      </table>'''

def dl(pary):
    return '\n        '.join(f'<div><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>' for a, b in pary)

def karta(k):
    sym = k['sym']; n = len(k['rows'])
    uw = ''.join(f'\n        <p class="kar-uwaga">{esc(u)}</p>' for u in k['uwagi'])
    inne = ' '.join(f'<a href="../{x["slug"]}/"' + (' aria-current="page"' if x is k else '') + f'>{esc(x["sym"])}</a>' for x in KARTY)
    ph = num(k['rows'][len(k['rows']) // 2][0])
    return f'''
<section class="sekcja pod-glowa">
  <div class="wrap">
    <nav class="okruchy" aria-label="Jesteś tutaj"><a href="../../">Strona główna</a><span>/</span><a href="../">Uszczelnienia techniczne</a><span>/</span><span aria-current="page">{esc(sym)}</span></nav>
    <div class="kar-gora">
      <figure class="kar-foto">
        <img src="../../img/u/{k['slug']}-zabudowa.webp" alt="{esc(sym)} - rysunek zabudowy z wymiarami" width="764" height="459" fetchpriority="high">
        <figcaption>Karta {esc(k['nr'])}</figcaption>
      </figure>
      <div class="kar-opis">
        <p class="kar-typ">{esc(k['typ'])}</p>
        <h1>{esc(sym)}</h1>
        <p>{esc(k['opis'])}</p>
        <p class="kar-zam">Zamawianie: <b>{esc(k['wzor'])}</b>, np. <b>{esc(k['przyklad'])}</b></p>
        <div class="kar-akcje"><a class="btn" href="../../#wycena"><span>Zapytaj o rozmiar</span></a><a class="kar-do-tab" href="#typoszereg">Tabela wymiarów ({n})</a></div>
      </div>
    </div>
  </div>
</section>

<section class="sekcja szara kar-dane">
  <div class="wrap kar-siatka">
    <div>
      <h2>Parametry pracy</h2>
      <dl class="kar-param">
        {dl(k['param'])}
      </dl>
    </div>
    <div>
      <h2>Konstrukcja</h2>
      <dl class="kar-param">
        {dl(k['konstr'])}
      </dl>
    </div>
  </div>
</section>

<section class="sekcja kar-tab" id="typoszereg">
  <div class="wrap">
    <div class="tab-glowa">
      <div class="tab-opis">
        <h2>Typoszereg {esc(sym)}</h2>
        <p class="kar-tol">Tolerancje gniazda: {esc(k['tol'])}.</p>{uw}
      </div>
      <div class="filtr">
        <label for="filtr-d">Szukaj po średnicy (mm)</label>
        <div class="filtr-pole"><input id="filtr-d" type="text" inputmode="decimal" autocomplete="off" placeholder="np. {esc(ph)}"><button type="button" id="filtr-x" hidden aria-label="Wyczyść">Wyczyść</button></div>
        <p id="filtr-info" class="filtr-info" aria-live="polite">{n} rozmiarów w typoszeregu</p>
      </div>
    </div>
    <p class="tab-hint">Tabelę można przesuwać w bok. Kolumna z oznaczeniem zostaje na miejscu.</p>
    <div class="tab-ramka" tabindex="0" role="region" aria-label="Tabela wymiarów {esc(sym)}, przewijana w poziomie">
      {tabela(k)}
    </div>
    <p id="filtr-brak" class="filtr-brak" hidden>Tego rozmiaru nie ma w typoszeregu. <a href="../../#wycena">Prosimy o zapytanie z wymiarami gniazda.</a></p>
    <p class="tab-przyp">Wymiary w mm według karty katalogowej {esc(k['nr'])}, wartości w nawiasach jak w karcie. Typoszereg zostanie uzupełniony o kolejne rozmiary.</p>
    <nav class="kar-inne" aria-label="Inne modele"><span>Inne karty:</span> {inne}</nav>
  </div>
</section>
'''
