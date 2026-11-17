# Buduje index.html (PL), en/index.html, de/index.html z jednego szablonu.
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = open(os.path.join(ROOT, '_src', 'index.src.html'), encoding='utf-8').read()

BADGE = open(os.path.join(ROOT, '_src', 'badge.html'), encoding='utf-8').read().strip()
HERO_SVG = open(os.path.join(ROOT, '_src', 'hero_rys.svg'), encoding='utf-8').read().strip()
BADGE_CSS = open(os.path.join(ROOT, '_src', 'badge_style.css'), encoding='utf-8').read().strip()

# ---------------- teksty ----------------
T = {}
T['pl'] = dict(
  lang='pl', p='', title='K-Tech Żory - obróbka CNC, hydraulika siłowa, kostki STECKO, uszczelnienia',
  desc='Obróbka skrawaniem CNC w Żorach: kostki i przyłącza STECKO, tłoki, dławice, produkcja uszczelnień technicznych, części obudów zmechanizowanych, konstrukcje spawane. Wycena z rysunku.',
  skip='Przejdź do treści', home='K-Tech - strona główna', firmaword='Przedsiębiorstwo Wielobranżowe',
  m_oferta='Oferta', m_usz='Uszczelnienia', usz_link='Modele i tabele wymiarów', m_maszyny='Maszyny', m_wyroby='Wyroby', m_wycena='Wycena', m_kontakt='Kontakt',
  menu_open='Otwórz menu', call='Zadzwoń',
  h1='Toczymy i frezujemy części, które pracują pod ciśnieniem',
  lead='Obróbka CNC w Żorach: kostki STECKO, tłoki, dławice, uszczelnienia i części obudów zmechanizowanych. Seryjnie albo według Państwa rysunku.',
  cta='Wyślij rysunek do wyceny', hero_alt='Centrum pionowe CNC podczas frezowania z chłodziwem',
  o_h='Co wykonujemy',
  o_p='Pięć obszarów, w których pracujemy na co dzień. Każdy wyrób z katalogu możemy wykonać w serii albo zmienić pod Państwa wymiary.',
  c1_h='Kostki i przyłącza STECKO', c1_p='Produkcja seryjna DN10 i DN12: kostki proste, niskie i wysokie kątowe, frezowane, zabezpieczające.',
  c2_h='Części na zamówienie', c2_p='Listwy przyłączeniowe, przyłącza stopniowe, specjalne i wkrętne, gniazda zaworów upustowych, sprzęgła, nakładki.',
  c3_h='Elementy siłowników', c3_p='Tłoki, dławice, tłoczyska i pierścienie dzielone do hydrauliki siłowej, z gwintami i rowkami pod uszczelnienia.',
  c4_h='Uszczelnienia techniczne', c4_p='Uszczelnienia tłoka DS, DSn, DZ, tłoczyska JS i JSn, pierścienie oporowe PO i zgarniające PZ, z tabelami wymiarów.',
  c5_h='Konstrukcje spawane i remonty', c5_p='Bębny zwrotne, konstrukcje spawane MIG, ślusarstwo oraz produkcja i remont części obudów zmechanizowanych.',
  ph='Zdjęcie', of='z',
  k_h='Park maszynowy',
  k_p='Pięć obrabiarek CNC i zaplecze konwencjonalne. Po zakresach osi od razu widać, czy Państwa detal zmieści się na naszych maszynach.',
  k_alt='Toczenie wałka na tokarce CNC',
  t_tok='Tokarka CNC', t_cen='Centrum pionowe CNC',
  s_avg='toczenie Ø 250 mm, długość 720 mm', s_avg2='toczenie Ø 450 mm, długość 300 mm',
  s_obr='8 000 obr/min',
  k_conv='Do tego tokarki uniwersalne, frezarki konwencjonalne i spawarki MIG.',
  w_h='Wybrane wyroby',
  w_p='Fragment katalogu. Pełne karty z tabelami wymiarów zostają na podstronach, jak dziś.',
  z_h='Wycena z rysunku',
  z_p='Najszybciej wycenimy detal, gdy dostaniemy rysunek, ilość i materiał.',
  z_l1='Prześlij rysunek (PDF, DXF, DWG, STEP) albo szkic z wymiarami.',
  z_l2='Podaj ilość sztuk i materiał, a jeśli to część zamienna, nazwę urządzenia.',
  z_l3='Odpowiemy wyceną i terminem wykonania.',
  z_stali='Stali klienci zamawiają przez konto w panelu zamówień. Konta zakładamy na podstawie umowy.',
  z_panel='Panel zamówień',
  f_name='Imię i nazwisko lub firma', f_mail='E-mail', f_tel='Telefon', f_ilosc='Ilość sztuk', f_mat='Materiał',
  f_mat_ph='np. stal C45, 42CrMo4, poliamid', f_msg='Czego dotyczy zapytanie', f_file='Dołącz rysunek',
  f_file_s='PDF, DXF, DWG, STEP, JPG', f_send='Wyślij zapytanie',
  f_demo='To podgląd strony, formularz niczego jeszcze nie wysyła. Zapytania prosimy kierować na biuro@k-tech.net.pl.',
  ko_h='Kontakt i dojazd', ko_firma='Przedsiębiorstwo Wielobranżowe K-TECH Krzysztof Fojcik',
  ko_kom='kom.', ko_tel='tel.', ko_fax='fax', ko_map='Mapa dojazdu do K-Tech, ul. Boczna 8, Żory',
  ko_zakres_h='Zakres działalności',
  ko_zakres=['Obróbka skrawaniem na obrabiarkach CNC i uniwersalnych', 'Produkcja elementów hydrauliki siłowej i sterowniczej', 'Produkcja uszczelnień technicznych', 'Produkcja i remont części obudów zmechanizowanych', 'Ślusarstwo i spawalnictwo'],
  ft_note='Zdjęcia obróbki na górze strony i w parku maszynowym są przykładowe, do zamiany na zdjęcia z zakładu w Żorach. Wyroby: rendery K-Tech.',
  ck_t='Mapa dojazdu korzysta z Google Maps, które może zapisywać pliki cookies.', ck_ok='Akceptuję', ck_no='Tylko niezbędne',
  bar_call='Zadzwoń', bar_cta='Wyślij rysunek',
  prev='Poprzednie', next='Następne',
)
T['en'] = dict(T['pl'],
  lang='en', p='../', title='K-Tech Żory, Poland - CNC machining, hydraulic components, STECKO blocks, seals',
  desc='CNC turning and milling in Żory, Poland: STECKO blocks and connectors, pistons, glands, technical seals, parts for powered roof supports, welded structures. Quotes from drawings.',
  skip='Skip to content', home='K-Tech - home', firmaword='Multi-trade company',
  m_oferta='Products', m_usz='Seals', usz_link='Models and size tables (PL)', m_maszyny='Machines', m_wyroby='Catalogue', m_wycena='Quote', m_kontakt='Contact',
  menu_open='Open menu', call='Call',
  h1='We turn and mill parts that work under pressure',
  lead='CNC machining in Żory, Poland: STECKO blocks, pistons, glands, seals and parts for powered roof supports. In series or to your drawing.',
  cta='Send a drawing for a quote', hero_alt='Vertical CNC machining centre milling with coolant',
  o_h='What we make',
  o_p='Five areas we work in every day. Any item from our catalogue can be made in series or adapted to your dimensions.',
  c1_h='STECKO blocks and connectors', c1_p='Series production DN10 and DN12: straight, low and high angle, milled and safety blocks.',
  c2_h='Custom parts', c2_p='Connection strips, stepped, special and screw-in connectors, relief valve seats, couplings, cover plates.',
  c3_h='Cylinder components', c3_p='Pistons, glands, piston rods and split rings for power hydraulics, with threads and seal grooves.',
  c4_h='Technical seals', c4_p='Piston seals DS, DSn, DZ, rod seals JS and JSn, back-up rings PO and wiper rings PZ, with size tables.',
  c5_h='Welded structures and repairs', c5_p='Return drums, MIG welded structures, metalwork, production and repair of powered roof support parts.',
  ph='Photo', of='of',
  k_h='Machine park',
  k_p='Five CNC machines plus conventional equipment. The axis travels show at a glance whether your part fits.',
  k_alt='Turning a shaft on a CNC lathe',
  t_tok='CNC lathe', t_cen='Vertical CNC machining centre',
  s_avg='turning Ø 250 mm, length 720 mm', s_avg2='turning Ø 450 mm, length 300 mm',
  s_obr='8,000 rpm',
  k_conv='Plus manual lathes, conventional milling machines and MIG welders.',
  w_h='Selected products',
  w_p='Part of our catalogue. Full product sheets with dimension tables stay on sub-pages.',
  z_h='Quote from a drawing',
  z_p='We can quote fastest when we receive a drawing, quantity and material.',
  z_l1='Send a drawing (PDF, DXF, DWG, STEP) or a dimensioned sketch.',
  z_l2='Give the quantity and material, and the machine name for spare parts.',
  z_l3='We reply with a price and lead time.',
  z_stali='Regular customers order through their account in the order panel. Accounts are set up under a contract.',
  z_panel='Order panel',
  f_name='Name or company', f_mail='E-mail', f_tel='Phone', f_ilosc='Quantity', f_mat='Material',
  f_mat_ph='e.g. C45 steel, 42CrMo4, polyamide', f_msg='Your enquiry', f_file='Attach a drawing',
  f_file_s='PDF, DXF, DWG, STEP, JPG', f_send='Send enquiry',
  f_demo='This is a website preview, the form does not send anything yet. Please write to biuro@k-tech.net.pl.',
  ko_h='Contact and directions', ko_firma='Przedsiębiorstwo Wielobranżowe K-TECH Krzysztof Fojcik',
  ko_kom='mobile', ko_tel='phone', ko_fax='fax', ko_map='Map to K-Tech, ul. Boczna 8, Żory, Poland',
  ko_zakres_h='Scope of work',
  ko_zakres=['Machining on CNC and manual machine tools', 'Power and control hydraulics components', 'Production of technical seals', 'Production and repair of powered roof support parts', 'Metalwork and welding'],
  ft_note='Machining photos at the top and in the machine park are placeholders, to be replaced with photos from the Żory plant. Products: K-Tech renders.',
  ck_t='The map uses Google Maps, which may store cookies.', ck_ok='Accept', ck_no='Essential only',
  bar_call='Call', bar_cta='Send drawing', prev='Previous', next='Next',
)
T['de'] = dict(T['pl'],
  lang='de', p='../', title='K-Tech Żory, Polen - CNC-Bearbeitung, Hydraulikteile, STECKO-Blöcke, Dichtungen',
  desc='CNC-Drehen und -Fräsen in Żory (Polen): STECKO-Blöcke und -Anschlüsse, Kolben, Führungsbuchsen, technische Dichtungen, Teile für Schreitausbau, Schweißkonstruktionen. Angebot nach Zeichnung.',
  skip='Zum Inhalt', home='K-Tech - Startseite', firmaword='Mehrbranchenunternehmen',
  m_oferta='Leistungen', m_usz='Dichtungen', usz_link='Modelle und Maßtabellen (PL)', m_maszyny='Maschinen', m_wyroby='Katalog', m_wycena='Anfrage', m_kontakt='Kontakt',
  menu_open='Menü öffnen', call='Anrufen',
  h1='Wir drehen und fräsen Teile, die unter Druck arbeiten',
  lead='CNC-Bearbeitung in Żory, Polen: STECKO-Blöcke, Kolben, Führungsbuchsen, Dichtungen und Teile für Schreitausbau. In Serie oder nach Ihrer Zeichnung.',
  cta='Zeichnung zur Anfrage senden', hero_alt='Vertikales CNC-Bearbeitungszentrum beim Fräsen mit Kühlschmierstoff',
  o_h='Was wir fertigen',
  o_p='Fünf Bereiche, in denen wir täglich arbeiten. Jedes Katalogteil fertigen wir in Serie oder passen es an Ihre Maße an.',
  c1_h='STECKO-Blöcke und Anschlüsse', c1_p='Serienfertigung DN10 und DN12: gerade, niedrige und hohe Winkelblöcke, gefräst, Sicherungsblöcke.',
  c2_h='Sonderteile', c2_p='Anschlussleisten, Stufen-, Sonder- und Einschraubanschlüsse, Sitze für Überdruckventile, Kupplungen, Auflagen.',
  c3_h='Zylinderteile', c3_p='Kolben, Führungsbuchsen, Kolbenstangen und geteilte Ringe für die Leistungshydraulik, mit Gewinden und Dichtungsnuten.',
  c4_h='Technische Dichtungen', c4_p='Kolbendichtungen DS, DSn, DZ, Stangendichtungen JS und JSn, Stützringe PO und Abstreifer PZ, mit Maßtabellen.',
  c5_h='Schweißkonstruktionen und Reparaturen', c5_p='Umlenktrommeln, MIG-Schweißkonstruktionen, Schlosserarbeiten, Fertigung und Reparatur von Teilen für Schreitausbau.',
  ph='Bild', of='von',
  k_h='Maschinenpark',
  k_p='Fünf CNC-Maschinen und konventionelle Ausstattung. An den Verfahrwegen sehen Sie sofort, ob Ihr Teil passt.',
  k_alt='Drehen einer Welle auf einer CNC-Drehmaschine',
  t_tok='CNC-Drehmaschine', t_cen='Vertikales CNC-Bearbeitungszentrum',
  s_avg='Drehen Ø 250 mm, Länge 720 mm', s_avg2='Drehen Ø 450 mm, Länge 300 mm',
  s_obr='8.000 U/min',
  k_conv='Dazu Universaldrehmaschinen, konventionelle Fräsmaschinen und MIG-Schweißgeräte.',
  w_h='Ausgewählte Produkte',
  w_p='Ein Auszug aus dem Katalog. Vollständige Datenblätter mit Maßtabellen bleiben auf den Unterseiten.',
  z_h='Angebot nach Zeichnung',
  z_p='Am schnellsten kalkulieren wir mit Zeichnung, Stückzahl und Werkstoff.',
  z_l1='Senden Sie eine Zeichnung (PDF, DXF, DWG, STEP) oder eine bemaßte Skizze.',
  z_l2='Nennen Sie Stückzahl und Werkstoff, bei Ersatzteilen auch die Maschine.',
  z_l3='Sie erhalten Preis und Liefertermin.',
  z_stali='Stammkunden bestellen über ihr Konto im Bestellportal. Konten richten wir auf Vertragsbasis ein.',
  z_panel='Bestellportal',
  f_name='Name oder Firma', f_mail='E-Mail', f_tel='Telefon', f_ilosc='Stückzahl', f_mat='Werkstoff',
  f_mat_ph='z. B. C45, 42CrMo4, Polyamid', f_msg='Ihre Anfrage', f_file='Zeichnung anhängen',
  f_file_s='PDF, DXF, DWG, STEP, JPG', f_send='Anfrage senden',
  f_demo='Dies ist eine Vorschau, das Formular sendet noch nichts. Bitte schreiben Sie an biuro@k-tech.net.pl.',
  ko_h='Kontakt und Anfahrt', ko_firma='Przedsiębiorstwo Wielobranżowe K-TECH Krzysztof Fojcik',
  ko_kom='Mobil', ko_tel='Tel.', ko_fax='Fax', ko_map='Karte zu K-Tech, ul. Boczna 8, Żory, Polen',
  ko_zakres_h='Leistungsumfang',
  ko_zakres=['Zerspanung auf CNC- und Universalmaschinen', 'Komponenten der Leistungs- und Steuerhydraulik', 'Herstellung technischer Dichtungen', 'Fertigung und Reparatur von Teilen für Schreitausbau', 'Schlosser- und Schweißarbeiten'],
  ft_note='Die Bearbeitungsfotos oben und im Maschinenpark sind Platzhalter und werden durch Fotos aus dem Werk in Żory ersetzt. Produkte: K-Tech-Renderings.',
  ck_t='Die Karte nutzt Google Maps, das Cookies speichern kann.', ck_ok='Akzeptieren', ck_no='Nur notwendige',
  bar_call='Anrufen', bar_cta='Zeichnung senden', prev='Zurück', next='Weiter',
)

# karty oferty: (klucz, [zdjecia])
CARDS = [
  ('c1', ['ktn-1','kwf-1','np-1','zab-1','ktnf-2']),
  ('c3', ['tlokgwin-1','dlaw130-1','dlaw9060-1','pierscdziel-1','tloczysko-2']),
  ('c2', ['kpl-1','skomp1-2','sprzeg-1','upust-1','przywk-1']),
  ('c4', ['jhs','ds','dsn','pz','po']),
  ('c5', ['btw-1','konspaw-1','tabspag-1','btw-2']),
]

# katalog: (zdjecie, pl, en, de, oznaczenie)
KAT = [
  ('ktn-2', 'Kostka STECKO niska kątowa', 'STECKO block, low angle', 'STECKO-Block, niedrig, Winkel', 'DN10 / DN12'),
  ('kwf-2', 'Kostka STECKO wysoka kątowa frez.', 'STECKO block, high angle, milled', 'STECKO-Block, hoch, Winkel, gefräst', 'DN10 / DN12'),
  ('np-2', 'Kostka STECKO prosta', 'STECKO block, straight', 'STECKO-Block, gerade', 'DN10 / DN12'),
  ('zab-3', 'Kostka STECKO zabezpieczająca', 'STECKO safety block', 'STECKO-Sicherungsblock', 'DN10 / DN12'),
  ('listw-1', 'Listwa przyłączeniowa', 'Connection strip', 'Anschlussleiste', 'DN10 / DN12'),
  ('przywk-2', 'Przyłącze wkrętne', 'Screw-in connector', 'Einschraubanschluss', 'DN12'),
  ('upust-3', 'Gniazdo zaworu upustowego', 'Relief valve seat', 'Sitz für Überdruckventil', ''),
  ('sprzeg-2', 'Sprzęgło', 'Coupling', 'Kupplung', ''),
  ('tlokgwin-2', 'Tłok 74', 'Piston 74', 'Kolben 74', 'M30x1,5'),
  ('tlok5951-1', 'Tłok 59/44', 'Piston 59/44', 'Kolben 59/44', 'M28x1,5'),
  ('dlaw130-2', 'Dławica 130/81,5', 'Gland 130/81.5', 'Führungsbuchse 130/81,5', ''),
  ('pierscdziel-2', 'Pierścień dzielony 73', 'Split ring 73', 'Geteilter Ring 73', ''),
  ('tul4b3-1', 'Tłok 89/56', 'Piston 89/56', 'Kolben 89/56', ''),
  ('btw-3', 'Bęben zwrotny', 'Return drum', 'Umlenktrommel', 'BTW-03.00'),
]

def esc(s): return html.escape(s, quote=True)

def cards(t):
    out = []
    for i, (k, imgs) in enumerate(CARDS):
        slides = []
        for j, im in enumerate(imgs):
            lazy = 'loading="lazy" ' if True else ''
            slides.append(f'<div class="sw-sl"><img src="{t["p"]}img/r/{im}.webp" alt="{esc(t[k+"_h"])}, {t["ph"].lower()} {j+1}" {lazy}decoding="async" width="638" height="415" draggable="false"></div>')
        big = ' karta-duza' if i == 0 else ''
        link = '\n' + f'  <a class="karta-link" href="{t["p"]}uszczelnienia/">{esc(t["usz_link"])}</a>' if k == 'c4' else ''
        out.append(f'''<article class="karta{big}">
  <div class="sw" data-of="{esc(t['of'])}">
    <div class="sw-tor" tabindex="0" aria-label="{esc(t[k+'_h'])}">{''.join(slides)}</div>
    <button class="sw-b sw-prev" type="button" aria-label="{esc(t['prev'])}"></button><button class="sw-b sw-next" type="button" aria-label="{esc(t['next'])}"></button>
    <span class="sw-n">1 {esc(t['of'])} {len(imgs)}</span>
  </div>
  <h3>{esc(t[k+'_h'])}</h3>
  <p>{esc(t[k+'_p'])}</p>{link}
</article>''')
    return '\n'.join(out)

def katalog(t):
    col = {'pl': 1, 'en': 2, 'de': 3}[t['lang']]
    out = []
    for row in KAT:
        name = row[col]; ozn = row[4]
        o = f'<span>{esc(ozn)}</span>' if ozn else ''
        out.append(f'<figure class="kat-el"><img src="{t["p"]}img/r/{row[0]}.webp" alt="{esc(name)}" loading="lazy" decoding="async" width="638" height="415" draggable="false"><figcaption><b>{esc(name)}</b>{o}</figcaption></figure>')
    return '\n'.join(out)

def zakres(t):
    return '\n'.join(f'        <li>{esc(x)}</li>' for x in t['ko_zakres'])

def build(code):
    t = T[code]
    s = TPL
    s = s.replace('[[ZAKRES]]', zakres(t))
    s = s.replace('[[CARDS]]', cards(t)).replace('[[KATALOG]]', katalog(t))
    s = s.replace('[[HERO_SVG]]', HERO_SVG)
    s = s.replace('[[BADGE]]', BADGE).replace('[[BADGE_CSS]]', BADGE_CSS)
    def rep(m):
        k = m.group(1)
        if k not in t: raise KeyError(k)
        return t[k] if k in ('p', 'lang') else esc(t[k])
    s = re.sub(r'\[\[([a-z0-9_]+)\]\]', rep, s)
    # przełącznik języków
    links = {'pl': {'pl': './', 'en': 'en/', 'de': 'de/'},
             'en': {'pl': '../', 'en': './', 'de': '../de/'},
             'de': {'pl': '../', 'en': '../en/', 'de': './'}}[code]
    sw = ''.join(f'<a href="{links[c]}" hreflang="{c}" lang="{c}"' + (' aria-current="page"' if c == code else '') + f'>{c.upper()}</a>' for c in ('pl', 'de', 'en'))
    s = s.replace('{{LANGS}}', sw)
    out = os.path.join(ROOT, 'index.html') if code == 'pl' else os.path.join(ROOT, code, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8', newline='\n').write(s)
    print('ok', out)

for c in ('pl', 'en', 'de'):
    build(c)
