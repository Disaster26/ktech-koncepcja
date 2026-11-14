# Buduje podstrony działu Uszczelnienia techniczne (podgląd PL):
#   uszczelnienia/index.html      - lista modeli
#   uszczelnienia/dsn/index.html  - przykładowa karta modelu z karty katalogowej KT-DSn01
# Nagłówek, logo i stopka są brane z gotowego index.html (uruchamiać po build.py).
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
esc = lambda s: html.escape(s, quote=True)

def wytnij(a, b):
    i = IDX.index(a); j = IDX.index(b, i) + len(b)
    return IDX[i:j]

HEAD_STYLE = wytnij('<style>', '</style>')
DEFS = wytnij('<svg width="0" height="0"', '</svg>')
HEADER = wytnij('<header class="top"', '</header>')
FOOTER = wytnij('<footer class="stopka">', '</footer>')

def przenies(s, p):
    s = re.sub(r'<a ([^>]*?)href="#(\w+)"', lambda m: f'<a {m.group(1)}href="{p}#{m.group(2)}"', s)
    s = s.replace('href="uszczelnienia/"', f'href="{p}uszczelnienia/"')
    s = s.replace('href="./"', f'href="{p}"').replace('href="de/"', f'href="{p}de/"').replace('href="en/"', f'href="{p}en/"')
    s = s.replace(f'href="{p}#start"', f'href="{p}"')
    return s

def strona(p, title, desc, body, aktywne=True):
    hdr = przenies(HEADER, p)
    if aktywne:
        hdr = hdr.replace(f'<a href="{p}uszczelnienia/">', f'<a href="{p}uszczelnienia/" class="akt" aria-current="page">', 1)
    ftr = przenies(FOOTER, p)
    ftr = re.sub(r'<p class="wrap st-nota">.*?</p>', '<p class="wrap st-nota">Rysunki: karty katalogowe K-Tech. Zdjęcia uszczelek do uzupełnienia.</p>', ftr, flags=re.S)
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#FFFFFF">
<link rel="preload" href="{p}fonts/barlow-semi-condensed-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}style.css">
<link rel="icon" href="{p}img/favicon.svg" type="image/svg+xml">
{HEAD_STYLE}
</head>
<body class="podstrona">
<a class="skip" href="#tresc">Przejdź do treści</a>

{DEFS}

{hdr}

<main id="tresc">
{body}
</main>

<div class="szew" aria-hidden="true"></div>
{ftr}

<script src="{p}app.js" defer></script>
</body>
</html>
'''

# ---------------- dział ----------------
MODELE = [
  ('Uszczelnienia tłoka', [
    ('ds', 'DS', 'Uszczelnienie tłoka', None),
    ('dsn', 'DSn', 'Uszczelnienie tłoka dwustronnego działania, wielokomponentowe, do 500 bar', 'dsn/'),
    ('dz', 'DZ', 'Uszczelnienie tłoka', None),
  ]),
  ('Uszczelnienia tłoczyska', [
    ('jsn', 'JSn', 'Uszczelnienie tłoczyska', None),
  ]),
  ('Pierścienie i uszczelki', [
    ('po', 'PO', 'Pierścień oporowy', None),
    ('pz', 'PZ', 'Pierścień zgarniający', None),
    ('up', 'UP', 'Uszczelka poliamidowa', None),
  ]),
]

def lista():
    out = []
    for grupa, modele in MODELE:
        el = []
        for img, nazwa, opis, link in modele:
            fig = f'<img src="../img/u/{img}.webp" alt="{esc(nazwa)} - rysunek zabudowy" width="638" height="390" loading="lazy" decoding="async">'
            if link:
                el.append(f'''<li class="mod mod-gotowy"><a href="{link}">{fig}<span class="mod-txt"><b>{esc(nazwa)}</b><span>{esc(opis)}</span><em>Karta i tabela wymiarów</em></span></a></li>''')
            else:
                el.append(f'''<li class="mod"><div>{fig}<span class="mod-txt"><b>{esc(nazwa)}</b><span>{esc(opis)}</span><em class="mod-wkrotce">Karta w przygotowaniu</em></span></div></li>''')
        out.append(f'''<section class="mod-grupa" aria-labelledby="g-{len(out)}">
      <h2 id="g-{len(out)}">{esc(grupa)}</h2>
      <ul class="mod-lista">
        {chr(10).join(el)}
      </ul>
    </section>''')
    return '\n    '.join(out)

dzial = f'''
<section class="sekcja pod-glowa">
  <div class="wrap">
    <nav class="okruchy" aria-label="Jesteś tutaj"><a href="../">Strona główna</a><span>/</span><a href="../#oferta">Oferta</a><span>/</span><span aria-current="page">Uszczelnienia techniczne</span></nav>
    <div class="pod-wstep">
      <div>
        <h1><i class="znak" aria-hidden="true"></i>Uszczelnienia techniczne</h1>
        <p>Uszczelnienia do hydrauliki siłowej i pneumatyki, w większości do siłowników górniczych. Każdy model ma kartę z parametrami pracy oraz tabelą wymiarów uszczelki i gniazda. Gdy potrzebnego rozmiaru nie ma w tabeli, prosimy o zapytanie z wymiarami gniazda.</p>
        <p class="pod-kontakt"><a href="tel:+48663005555">663 005 555</a><a href="mailto:biuro@k-tech.net.pl">biuro@k-tech.net.pl</a></p>
      </div>
      <figure class="pod-profil"><img src="../img/u/dsn-profil.webp" alt="Przekrój uszczelnienia DSn" width="638" height="232" fetchpriority="high"><figcaption>DSn w przekroju: część czołowa, część dolna i pierścienie przeciwwyciskowe</figcaption></figure>
    </div>
  </div>
</section>

<section class="sekcja mod-sekcja">
  <div class="wrap">
    {lista()}
    <p class="mod-nota">W podglądzie gotowa jest przykładowa karta DSn. Pozostałe modele zostaną uzupełnione z kart katalogowych K-Tech, a kolejne można dodawać samodzielnie w panelu strony.</p>
  </div>
</section>
'''

# ---------------- karta DSn (dane: karta KT-DSn01) ----------------
WIERSZE = '''110|99|12|109,4|99|110|13|1|0,5
120|105|15|119,4|105|120|16|1|0,5
200|175|(32)25|199|175|200|(33)26|1|0,5
201,2|175|(32)25|199|175|201,2|(33)26|1|0,5
202,5|175|(32)25|199|175|202,5|(33)26|1|0,5
203,8|175|(32)25|199|175|203,8|(33)26|1|0,5
200|180|15|199|180|200|16|1|0,5
245|220|25|244|220|245|26|1|0,5
250|220|(38)25|249|220|250|(39)26|1|0,5
250|225|(25)24|249|225|250|(26)25|1|0,5
251,2|220|(38)25|249|220|251,2|(39)26|1|0,5
252,5|220|(38)25|249|220|252,5|(39)26|1|0,5
253,8|220|(38)25|249|220|253,8|(39)26|1|0,5
255|220|(38)25|249|220|255|(39)26|1|0,5
260|235|25|259|235|260|26|1|0,5
290|265|25|289|265|290|26|1|0,5
300|275|25|299|275|320|26|1|0,5
320|290|30|319|290|320|31|1|0,5'''.split('\n')

def h_ozn(h):
    m = re.match(r'\((\d+)\)(\d+)', h)
    return m.group(2) if m else h

def tabela():
    rows = []
    for w in WIERSZE:
        c = w.split('|')
        ozn = f'DSn {c[0]} x {c[1]} x {h_ozn(c[2])}'
        td = ''.join(f'<td{" class=\"zab\"" if k >= 3 else ""}>{esc(v)}</td>' for k, v in enumerate(c))
        rows.append(f'<tr data-d1="{c[0]}" data-d2="{c[1]}" data-d3="{c[5]}"><th scope="row">{ozn}</th>{td}</tr>')
    return '\n          '.join(rows)

KOL = [('d1', 'średnica zewnętrzna'), ('d2', 'średnica wewnętrzna'), ('h', 'szerokość uszczelki'),
       ('D1', 'średnica zewnętrzna tłoka'), ('D2', 'średnica dna gniazda'), ('D3', 'średnica cylindra'),
       ('L', 'szerokość gniazda'), ('R', 'promień wewnętrzny'), ('r', 'promień zewnętrzny')]
thead2 = ''.join(f'<th scope="col"{" class=\"zab\"" if k >= 3 else ""}><b>{s}</b><span>{esc(o)}</span></th>' for k, (s, o) in enumerate(KOL))

dsn = f'''
<section class="sekcja pod-glowa">
  <div class="wrap">
    <nav class="okruchy" aria-label="Jesteś tutaj"><a href="../../">Strona główna</a><span>/</span><a href="../">Uszczelnienia techniczne</a><span>/</span><span aria-current="page">DSn</span></nav>
    <div class="kar-gora">
      <figure class="kar-foto">
        <img src="../../img/u/dsn-profil.webp" alt="Uszczelnienie tłoka DSn w przekroju" width="638" height="232" fetchpriority="high">
        <figcaption>Karta KT-DSn01</figcaption>
      </figure>
      <div class="kar-opis">
        <p class="kar-typ">Uszczelnienie tłoka</p>
        <h1>DSn</h1>
        <p>Element uszczelniający wielokomponentowy, dwustronnego działania. Wysokociśnieniowa uszczelka wykonana z materiałów termoplastycznych. Stosowana głównie w siłownikach górniczych, a typoszereg standardowy także w hydraulice innych gałęzi przemysłu.</p>
        <p class="kar-zam">Zamawianie: <b>d1 x d2 x h</b>, np. <b>DSn 250 x 220 x 25</b></p>
        <div class="kar-akcje"><a class="btn" href="../../#wycena"><span>Zapytaj o rozmiar</span></a><a class="kar-do-tab" href="#typoszereg">Tabela wymiarów</a></div>
      </div>
    </div>
  </div>
</section>

<section class="sekcja szara kar-dane">
  <div class="wrap kar-siatka">
    <div>
      <h2>Parametry pracy</h2>
      <dl class="kar-param">
        <div><dt>Ciśnienie</dt><dd>500 bar / 50 MPa</dd></div>
        <div><dt>Temperatura pracy</dt><dd>-30 ÷ +90 °C</dd></div>
        <div><dt>Prędkość ruchu</dt><dd>do 0,5 m/s</dd></div>
        <div><dt>Medium</dt><dd>oleje mineralne; emulsje olejowo-wodne HFA, HFB, HFC; wodny roztwór glikolu etylowego, np. Polikon Test</dd></div>
      </dl>
    </div>
    <div>
      <h2>Konstrukcja</h2>
      <dl class="kar-param">
        <div><dt>Część dolna</dt><dd>TPU-80 lub NBR-75 Shore A</dd></div>
        <div><dt>Część czołowa</dt><dd>TPU-92 Shore A</dd></div>
        <div><dt>Pierścień przeciwwyciskowy</dt><dd>POM</dd></div>
        <div><dt>Cechy</dt><dd>wysoka odporność na ścieranie; poliacetalowe pierścienie zabezpieczające przed wyciskaniem; pierścienie oporowe opcjonalnie z jednej lub z dwóch stron</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="sekcja kar-zabudowa">
  <div class="wrap kar-siatka">
    <figure class="kar-rys"><img src="../../img/u/dsn.webp" alt="Wymiary zabudowy uszczelnienia DSn: ØD3 H10, ØD1, ØD2 h10, L, R, r" width="638" height="395" loading="lazy" decoding="async"></figure>
    <div>
      <h2>Wymiary zabudowy</h2>
      <p class="kar-tol">Tolerancje gniazda: ØD3 H10, ØD2 h10, ØD1 -0,2, L +0,2.</p>
      <p class="kar-uwaga">W zależności od szerokości gniazda stosowane są pierścienie przeciwwyciskowe (dla szerokości 25 mm) lub pierścienie przeciwwyciskowo-oporowe (dla szerokości 32 i 38 mm).</p>
    </div>
  </div>
</section>

<section class="sekcja kar-tab" id="typoszereg">
  <div class="wrap">
    <div class="tab-glowa">
      <h2>Typoszereg DSn</h2>
      <div class="filtr">
        <label for="filtr-d">Szukaj po średnicy (mm)</label>
        <div class="filtr-pole"><input id="filtr-d" type="text" inputmode="decimal" autocomplete="off" placeholder="np. 250"><button type="button" id="filtr-x" hidden aria-label="Wyczyść">Wyczyść</button></div>
        <p id="filtr-info" class="filtr-info" aria-live="polite">18 rozmiarów w typoszeregu</p>
      </div>
    </div>
    <p class="tab-hint">Tabelę można przesuwać w bok. Kolumna z oznaczeniem zostaje na miejscu.</p>
    <div class="tab-ramka" tabindex="0" role="region" aria-label="Tabela wymiarów DSn, przewijana w poziomie">
      <table id="tab-wym" class="tab-wym">
        <thead>
          <tr class="tab-grupy"><th scope="col" rowspan="2" class="tab-ozn">Oznaczenie</th><th colspan="3" scope="colgroup">Uszczelka</th><th colspan="6" scope="colgroup" class="zab">Gniazdo (zabudowa)</th></tr>
          <tr>{thead2}</tr>
        </thead>
        <tbody>
          {tabela()}
        </tbody>
      </table>
    </div>
    <p id="filtr-brak" class="filtr-brak" hidden>Tego rozmiaru nie ma w typoszeregu. <a href="../../#wycena">Prosimy o zapytanie z wymiarami gniazda.</a></p>
    <p class="tab-przyp">Wymiary w mm według karty katalogowej KT-DSn01, wartości w nawiasach jak w karcie.</p>
  </div>
</section>
'''

def zapisz(rel, s):
    out = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8', newline='\n').write(s)
    print('ok', out)

zapisz('uszczelnienia/index.html', strona('../', 'Uszczelnienia techniczne - K-Tech Żory', 'Uszczelnienia tłoka DS, DSn, DZ, tłoczyska JSn, pierścienie oporowe PO i zgarniające PZ, uszczelki poliamidowe UP. Karty z tabelami wymiarów.', dzial))
zapisz('uszczelnienia/dsn/index.html', strona('../../', 'DSn uszczelnienie tłoka - wymiary i parametry - K-Tech', 'Uszczelnienie tłoka DSn: 500 bar, -30 do +90 °C, 0,5 m/s. Tabela wszystkich wymiarów uszczelki i gniazda.', dsn))
