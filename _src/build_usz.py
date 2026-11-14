# Buduje podstrony działu Uszczelnienia techniczne (podgląd PL):
#   uszczelnienia/index.html      - lista modeli
#   uszczelnienia/<model>/index.html - karty modeli z kart katalogowych K-Tech (dane: karty_dane.py)
# Nagłówek, logo i stopka są brane z gotowego index.html (uruchamiać po build.py).
import os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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

from usz_strony import dzial, karta, KARTY

def zapisz(rel, s):
    out = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8', newline='\n').write(s)
    print('ok', rel)

zapisz('uszczelnienia/index.html', strona('../', 'Uszczelnienia techniczne - K-Tech Żory', 'Uszczelnienia tłoka DS, DSn, DZ, tłoczyska JS, JSn, pierścienie oporowe PO i zgarniające PZ. Karty z parametrami i tabelami wymiarów.', dzial()))
for k in KARTY:
    zapisz('uszczelnienia/%s/index.html' % k['slug'], strona('../../', '%s %s - wymiary i parametry - K-Tech' % (k['sym'], k['typ'].lower()), '%s, %s: parametry pracy, materiał i tabela %d rozmiarów uszczelki i gniazda.' % (k['sym'], k['typ'].lower(), len(k['rows'])), karta(k)))
