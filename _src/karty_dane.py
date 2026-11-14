# Dane przepisane z kart katalogowych K-Tech (maile 14.11.2026, 10:26).
# Tabele przepisane z renderów kart (300 dpi), bez zmian wartości.

MEDIUM = 'oleje mineralne; emulsje olejowo-wodne HFA, HFB, HFC; wodny roztwór glikolu etylowego, np. Polikon Test'

# kolumny: (symbol, opis z karty)
K_TLOK = [('d1', 'średnica zewnętrzna'), ('d2', 'średnica wewnętrzna'), ('h', 'szerokość uszczelki'),
          ('D1', 'średnica zewnętrzna'), ('D2', 'średnica wewnętrzna'), ('D3', 'średnica cylindra'),
          ('L', 'szerokość gniazda'), ('R', 'promień wewnętrzny'), ('r', 'promień zewnętrzny')]
K_TLOCZ = [('d1', 'średnica wewnętrzna'), ('d2', 'średnica zewnętrzna'), ('h', 'szerokość uszczelki'),
           ('D1', 'średnica wewnętrzna'), ('D2', 'średnica zewnętrzna'), ('D3', 'średnica tłoczyska'),
           ('L', 'szerokość gniazda'), ('R', 'promień wewnętrzny'), ('r', 'promień zewnętrzny')]
K_PZ = [('d1', 'średnica wewnętrzna'), ('d2', 'średnica zewnętrzna'), ('h1', 'szerokość uszczelki'), ('h2', 'szerokość części trzymającej'),
        ('D1', 'średnica wewnętrzna'), ('D2', 'średnica zewnętrzna'), ('D3', 'średnica tłoczyska'),
        ('L', 'szerokość gniazda'), ('R', 'promień wewnętrzny'), ('r', 'promień zewnętrzny')]

def T(s):
    return [r.split() for r in s.strip().split('\n')]

KARTY = [
dict(slug='ds', sym='DS', typ='Uszczelnienie tłoka', nr='KT-DS01', kol=K_TLOK, usz=3,
  opis='Element uszczelniający wielokomponentowy, dwustronnego działania, zabudowa na tłok dzielony. Wysokociśnieniowa uszczelka wykonana z materiałów termoplastycznych. Stosowana głównie w siłownikach górniczych, a typoszereg standardowy także w hydraulice innych gałęzi przemysłu.',
  param=[('Ciśnienie', '500 bar / 50 MPa'), ('Temperatura pracy', '-30 ÷ +90 °C'), ('Prędkość ruchu', 'do 0,5 m/s'), ('Medium', MEDIUM)],
  konstr=[('Materiał', 'TPU-92 Shore A'), ('Pierścień przeciwwyciskowy', 'POM'),
          ('Cechy', 'wysoka odporność na ścieranie; poliacetalowe pierścienie zabezpieczające przed wyciskaniem; pierścienie oporowe opcjonalnie z jednej lub z dwóch stron')],
  tol='ØD3 H10, ØD2 h10, ØD1 -0,2, L +0,2',
  uwagi=['W zależności od szerokości gniazda stosowane są pierścienie przeciwwyciskowe (dla szerokości 25 mm) lub pierścienie przeciwwyciskowo-oporowe (dla szerokości 32 i 38 mm).', 'Pozostałe wymiary na zapytanie.'],
  wzor='d1 x d2 x h', przyklad='DS 120 x 100 x 25',
  rows=T('''
63 46 8 62 46 63 9 0,5 0,2
75 55 25 73,6 55 75 31 0,5 0,2
90 70 25 89 70 90 31 0,5 0,2
120 100 25 118,5 100 120 36 0,5 0,2
121 100 25 118,5 100 121 36 0,5 0,2
135 110 32 133,5 110 135 43 0,5 0,2
136 110 32 133,5 110 136 43 0,5 0,2
137,5 110 32 133,5 110 137,5 43 0,5 0,2
160 135 32 158,5 135 160 43 0,5 0,2
161,2 135 32 158,5 135 161,2 43 0,5 0,2
162,5 135 32 158,5 135 162,5 43 0,5 0,2
163,8 135 32 158,5 135 163,8 43 0,5 0,2
170 145 32 168,5 145 170 43 0,5 0,2
200 175 32 198,5 175 200 43 0,8 0,2
201,2 175 32 198,5 175 201,2 43 0,8 0,2
202,5 175 32 198,5 175 202,5 43 0,8 0,2
203,8 175 32 198,5 175 203,8 43 0,8 0,2
250 220 38 249 220 250 49 0,8 0,5
251 220 38 249 220 251 49 0,8 0,5
252,5 220 38 249 220 252,5 49 0,8 0,5
253,8 220 38 249 220 253,8 49 0,8 0,5
255 220 38 249 220 255 49 0,8 0,5''')),

dict(slug='dsn', sym='DSn', typ='Uszczelnienie tłoka', nr='KT-DSn01', kol=K_TLOK, usz=3,
  opis='Element uszczelniający wielokomponentowy, dwustronnego działania, zabudowa na tłok stały. Wysokociśnieniowa uszczelka wykonana z materiałów termoplastycznych. Stosowana głównie w siłownikach górniczych, a typoszereg standardowy także w hydraulice innych gałęzi przemysłu.',
  param=[('Ciśnienie', '500 bar / 50 MPa'), ('Temperatura pracy', '-30 ÷ +90 °C'), ('Prędkość ruchu', 'do 0,5 m/s'), ('Medium', MEDIUM)],
  konstr=[('Część dolna', 'TPU-80 lub NBR-80 Shore A'), ('Część czołowa', 'TPU-95 Shore A'), ('Pierścień przeciwwyciskowy', 'POM'),
          ('Cechy', 'wysoka odporność na ścieranie; poliacetalowe pierścienie zabezpieczające przed wyciskaniem; pierścienie oporowe opcjonalnie z jednej lub z dwóch stron')],
  tol='ØD3 H10, ØD2 h10, ØD1 -0,2, L +0,2, h +0,2 / +0,1',
  uwagi=['W zależności od szerokości gniazda stosowane są pierścienie przeciwwyciskowe (dla szerokości 25 mm) lub pierścienie przeciwwyciskowo-oporowe (dla szerokości 32 i 38 mm).',
         'Uszczelnienia z tabeli wykonane metodą wtrysku. Nadwymiary wykonane metodą Seal-Jet, na zapytanie.', 'Pozostałe wymiary na zapytanie.'],
  wzor='d1 x d2 x h', przyklad='DSn 250 x 220 x 25',
  rows=T('''
75 55 22 74,4 55 75 23 1 0,5
90 75 12,5 89,4 75 90 13,5 1 0,5
110 99 12 109,4 99 110 13 1 0,5
120 105 15 119,4 105 120 16 1 0,5
135 120 15 134,4 120 110 16 1 0,5
150 133 19 149,4 133 150 20 1 0,5
195 175 15 194 175 195 16 1 0,5
200 180 15 199 180 200 16 1 0,5
230 205 (25)24 229 205 230 (26)25 1 0,5
240 215 (25)24 239 215 240 (26)25 1 0,5
250 220 (38)25 249 220 250 (39)26 1 0,5
250 225 (25)24 249 225 250 (26)25 1 0,5
251,2 225 (25)24 249 225 251,2 (26)25 1 0,5
252,5 225 (25)24 249 225 252,5 (26)25 1 0,5
260 235 (25)24 259 235 260 (26)25 1 0,5
275 250 (25)24 274 250 275 (26)25 1 0,5
280 255 (25)24 279 255 280 (26)25 1 0,5
290 265 (25)24 289 265 290 (26)25 1 0,5
300 275 (25)24 299 275 300 (26)25 1 0,5
320 290 29 319 290 320 30 1 0,5''')),

dict(slug='dz', sym='DZ', typ='Uszczelnienie tłoka', nr='KT-DZ01', kol=K_TLOK, usz=3,
  opis='Uszczelnienie DZ-Usmt jest elementem uszczelniającym jednokomponentowym, dwustronnego działania, zabudowa na tłok stały. Wysokociśnieniowa uszczelka wykonana z materiałów termoplastycznych. Stosowana głównie w siłownikach górniczych, a typoszereg standardowy także w hydraulice innych gałęzi przemysłu.',
  param=[('Ciśnienie', '500 bar / 50 MPa'), ('Temperatura pracy', '-30 ÷ +90 °C'), ('Prędkość ruchu', 'do 0,5 m/s'), ('Medium', MEDIUM)],
  konstr=[('Część uszczelniająca', 'TPU-92 Shore A'), ('Pierścień przeciwwyciskowy', 'POM'),
          ('Cechy', 'wysoka odporność na ścieranie; poliacetalowe pierścienie zabezpieczające przed wyciskaniem')],
  tol='ØD3 H10, ØD2 h10, ØD1 -0,2, L +0,5, faza 30°',
  uwagi=['Do montażu zalecana jest faza montażowa min. 15°, maks. 30°, o szerokości około 10 mm.', 'Pozostałe wymiary na zapytanie.'],
  wzor='d1 x d2 x h', przyklad='DZ 210 x 190 x 15',
  rows=T('''
90 80 8 89 80 120 9 0,5 0,2
120 102 15 119 102 120 16 0,5 0,2
120 105 12 119 105 120 13 0,5 0,2
120 105 15 119 105 120 16 0,5 0,2
125 110 15 124 110 120 16 0,5 0,2
135 120 15 134 120 135 16 0,5 0,2
160 145 15 159 145 160 16 0,5 0,2
161,2 145 15 160 145 161,2 16 0,5 0,2
162,5 145 15 161,5 145 162,5 16 0,5 0,2
200 180 15 199 180 200 16 0,5 0,2
210 190 15 209 190 210 16 0,5 0,2
211,2 190 15 210 190 211,2 16 0,5 0,2
212,5 190 15 211,5 190 212,5 16 0,5 0,2''')),

dict(slug='po', sym='PO', typ='Pierścień oporowy', nr='KT-PO01', kol=K_TLOK, usz=3,
  opis='Pierścień PO jest stosowany wspólnie z uszczelnieniem DS lub DSn. W zależności od typu siłownika pierścienie stosuje się z jednej strony uszczelki lub po obu stronach. Jako osobny element nie występuje.',
  param=[('Temperatura pracy', '-30 ÷ +110 °C'), ('Prędkość ruchu', 'do 0,5 m/s'), ('Medium', MEDIUM)],
  konstr=[('Materiał', 'POM'),
          ('Cechy', 'wysoka odporność na ścieranie; dobre właściwości przy pracy bez smarowania; duża wytrzymałość na ściskanie; odporność na substancje chemiczne')],
  tol='ØD3 H10, ØD2 h10, ØD1 -0,2, L +0,2',
  uwagi=[],
  wzor='d1 x d2 x h', przyklad='PO 120 x 100 x 5',
  rows=T('''
75 55 5 73,6 55 75 31 0,5 0,2
75,8 71 3 75 71 75,8 3 0,5 0,2
90 70 5 89 70 90 31 0,5 0,2
90 75 5 89 75 90 31 0,5 0,2
110 95 5 108,5 95 110 31 0,5 0,2
120 100 5 118,5 100 120 36 0,5 0,2
135 110 5 133,5 110 135 43 0,5 0,2
160 135 5 158,5 135 160 43 0,5 0,2
161 135 5 159,5 135 161,2 43 0,5 0,2
170 145 5 168,5 145 170 43 0,8 0,2
125 115,8 2 124 115,8 125 2 0,8 0,2
120 110,8 3 119 110,8 120 3 0,8 0,2
200 175 5 198,5 175 200 43 0,8 0,2
202,5 175 5 198,5 175 202,5 43 0,8 0,2
203,8 175 5 198,5 175 203,8 43 0,8 0,2
205 175 5 198,5 175 205 43 0,8 0,2
240 228,8 3,5 238,5 228,8 240 3,5 0,8 0,2
250 220 5 248,5 220 250 49 1 0,2
252,5 220 5 248,5 220 252,5 49 1 0,2
255 220 5 248,5 220 255 49 1 0,2
280 255 6 278,5 255 280 32 1 0,2
290 278,8 4 288,5 278,8 290 4 1 0,2
320 290 5 318,5 290 320 32 1 0,2
321 290 5 318,5 290 321,2 32 1 0,2''')),

dict(slug='js', sym='JS', typ='Uszczelnienie tłoczyska', nr='KT-JS-2', kol=K_TLOCZ, usz=3,
  opis='Element uszczelniający jednokomponentowy, jednostronnego działania. Wysokociśnieniowa uszczelka wykonana z materiałów termoplastycznych. Stosowana głównie w siłownikach górniczych, a typoszereg standardowy także w hydraulice innych gałęzi przemysłu.',
  param=[('Ciśnienie', '500 bar / 50 MPa'), ('Temperatura pracy', '-30 ÷ +90 °C'), ('Prędkość ruchu', 'do 0,5 m/s'), ('Medium', MEDIUM)],
  konstr=[('Materiał', 'TPU 88 ÷ 90 Shore A'), ('Pierścień przeciwwyciskowy', 'POM'),
          ('Cechy', 'wysoka odporność na ścieranie; poliacetalowy pierścień zabezpieczający przed wyciskaniem')],
  tol='ØD2 H10, ØD1 +0,2, ØD3 h10, L +0,2, R 0,5, r 0,5',
  uwagi=[],
  wzor='d1 x d2 x h', przyklad='JS 100 x 115 x 11',
  rows=T('''
38,8 55 11 40 55 38,8 11,8 0,5 0,2
40 55 11 41,5 55 40 11,8 0,5 0,2
61,8 78 11 63 78 61,8 11,8 0,5 0,2
63 73 8 64,5 73 63 9 0,5 0,2
63 75 8,6 64,5 75 63 9,6 0,5 0,2
63 78 11 64,5 78 63 11,8 0,5 0,2
78,8 100 14 80 100 78,8 14,8 0,5 0,2
80 90 8 81,5 90 80 9 0,5 0,2
80 100 14 81,5 100 80 14,8 0,5 0,2
97,5 115 11 98,8 115 100 11,8 0,5 0,2
98,8 115 11 100 115 98,8 11,8 0,5 0,2
100 115 11 101,5 115 100 11,8 0,5 0,2
115 130 14,5 116,5 130 115 16 0,5 0,2''')),

dict(slug='jsn', sym='JSn', typ='Uszczelnienie tłoczyska', nr='KT-JS01', kol=K_TLOCZ, usz=3,
  opis='Element uszczelniający wielokomponentowy, jednostronnego działania. Wysokociśnieniowa uszczelka wykonana z materiałów termoplastycznych, z wypełniaczem zacisku wstępnego o przekroju kołowym. Stosowana głównie w siłownikach górniczych, a typoszereg standardowy także w hydraulice innych gałęzi przemysłu.',
  param=[('Ciśnienie', '500 bar / 50 MPa'), ('Temperatura pracy', '-30 ÷ +90 °C'), ('Prędkość ruchu', 'do 0,5 m/s'), ('Medium', MEDIUM)],
  konstr=[('Materiał', 'TPU 88 ÷ 90 Shore A'), ('Pierścień przeciwwyciskowy', 'POM'), ('Wypełniacz', 'NBR70'),
          ('Cechy', 'wysoka odporność na ścieranie; poliacetalowy pierścień zabezpieczający przed wyciskaniem; wypełniacz zacisku wstępnego')],
  tol='ØD2 H10, ØD1 +0,2, ØD3 h10, L +0,5, R 0,5, r 0,5',
  uwagi=['Pozostałe wymiary na zapytanie.'],
  wzor='d1 x d2 x h', przyklad='JSn 200 x 220 x 14,5',
  rows=T('''
38,8 55 11 40 55 38,8 11,8 0,5 0,2
40 50 11 41,5 50 40 11,8 0,5 0,2
40 55 11 41,5 55 40 11,8 0,5 0,2
40 60 8 41,5 59,6 40 9 0,5 0,2
61,8 78 11 63 78 61,8 11,8 0,5 0,2
63 78 11 64,5 78 63 11,8 0,5 0,2
78,8 100 14 80 100 78,8 14,8 0,5 0,2
80 100 14 81,5 100 80 14,8 0,5 0,2
97,5 115 11 98,8 115 97,5 11,8 0,5 0,2
98,8 115 11 100 115 98,8 11,8 0,5 0,2
100 115 11 101,5 115 100 11,8 0,5 0,2
115 135 13,6 116,5 135 115 14,5 0,5 0,2
160 180 14,5 161,5 180 160 16 0,8 0,2
180 195 14,5 181,5 195 180 16 0,8 0,2
190 220 22 191,5 220 190 22,8 0,8 0,2
190 222 22 191,5 222 190 22,8 0,8 0,2
195 210 22 196,5 210 195 22,8 0,8 0,2
197,5 220 14,5 199 220 197,5 16 0,8 0,2
198,8 220 14,5 220,3 220 198,8 16 0,8 0,2
200 220 14,5 221,5 220 200 16 0,8 0,2
220 240 14,5 221,5 240 220 16 1 0,2
230 250 14,5 231,5 250 230 16 1 0,2
237,5 260 14,5 239 260 237,5 16 1 0,2
238,8 260 14,5 241 260 238,8 16 1 0,2
240 260 14,5 241,5 260 240 16 1 0,2
242,5 270 18 244 270 242,5 20 1 0,2
243,8 270 18 246,5 270 243,8 20 1 0,2
245 270 18 246,5 270 245 20 1 0,2
265 285 14,5 266,5 285 265 16 1 0,2
266 286 14,5 267,5 286 266 16 1 0,2
280 300 14,5 281,5 300 280 16 1 0,2
285 305 14,5 286,5 305 285 16 1 0,2
285 310 16,4 286,5 310 285 18 1 0,2
290 310 16,4 291,5 310 290 18 1 0,2
303,8 325 16,4 306,5 325 303,8 18 1 0,2
302,5 325 16,4 306,5 325 302,5 18 1 0,2
305 325 16,4 306,5 325 305 18 1 0,2''')),

dict(slug='pz', sym='PZ', typ='Pierścień zgarniający', nr='KT-PZ01', kol=K_PZ, usz=4,
  opis='Pierścienie zgarniające PZ stosowane są w siłownikach hydraulicznych pracujących w ruchu posuwisto-zwrotnym. Ich zadaniem jest usuwanie nagromadzonych na tłoczysku zanieczyszczeń, takich jak błoto czy lód.',
  param=[('Temperatura pracy', '-40 ÷ +120 °C'), ('Prędkość ruchu', 'do 4,0 m/s'), ('Medium', MEDIUM)],
  konstr=[('Pierścień zgarniający', 'TPU, twardość zależnie od zastosowania 59 ÷ 65 Shore D'),
          ('Cechy', 'wysoka odporność na ścieranie; skuteczna krawędź zgarniająca; materiał odporny na trudne warunki eksploatacyjne')],
  tol='ØD2 H10, ØD1 +0,2, ØD3 h10, L +0,2',
  uwagi=[],
  wzor='d1 x d2 x h1 x h2', przyklad='PZ 100 x 110 x 10 x 7',
  rows=T('''
38,8 50 10 7 40 50 38,8 7,2 0,5 0,2
40 50 10 7 41,5 50 40 7,2 0,5 0,2
61 75 10 7 62,2 75 61 7,2 0,5 0,2
61,8 75 10 7 63 75 63 7,2 0,5 0,2
63 75 10 7 64,5 75 63 7,2 0,5 0,2
63 73 9 6 64,5 73 63 6,2 0,5 0,2
80 90 10 8 81,5 90 80 7,2 0,5 0,2
97,5 110 10 7 98,8 110 97,5 7,2 0,5 0,2
98,8 110 10 7 100 110 98,8 7,2 0,5 0,2
100 110 10 7 101,5 110 100 7,2 0,5 0,2
190 205 14 10 191 205 190 10,2 0,5 0,2
195 210 16 10 196 210 195 10,2 0,5 0,2
198,8 220 16 12 201 220 198,8 12,2 0,5 0,2
200 220 16 12 201 220 200 12,2 0,5 0,2
220 235 14 10 221 235 220 10,2 0,5 0,2
237,5 260 18 12 241 260 237,5 12,2 0,5 0,2
238,8 260 18 12 241 260 238,8 12,2 0,5 0,2
245 255 12 10 245 255 245 10,2 0,5 0,2
285 305 18 12,3 286,5 305 285 12,5 0,5 0,2
305 325 18 12 306,5 325 305 12,2 0,5 0,2''')),
]

# Spis podstawowych profili (strona 1 katalogu): (symbol, typ, materiał, slug karty lub None, profil)
SPIS = [
  ('DS', 'Uszczelnienie tłoka', 'TPU/POM', 'ds', 'ds'),
  ('DSn', 'Uszczelnienie tłoka', 'TPU/POM', 'dsn', 'dsn'),
  ('DZ', 'Uszczelnienie tłoka', 'TPU/POM', 'dz', 'dz'),
  ('PO', 'Pierścień oporowy', 'POM', 'po', 'po'),
  ('PP', 'Pierścień prowadzący tłokowy', 'POM', None, 'pp'),
  ('WFE', 'Pierścień prowadzący tłokowy z kanałami', 'POM', None, 'wfe'),
  ('JSn', 'Uszczelnienie tłoczyska', 'TPU/NBR/POM', 'jsn', 'jsn'),
  ('JS', 'Uszczelnienie tłoczyska', 'TPU/POM', 'js', 'js'),
  ('PZ', 'Pierścień zgarniający', 'TPU', 'pz', 'pz'),
  ('PP', 'Pierścień prowadzący tłoczyskowy', 'POM', None, 'pp'),
  ('PW', 'Pierścień prowadzący tłoczyskowy, profilowy', 'POM', None, 'pw'),
  ('PE', 'Pierścień podporowy', 'POM / PTFE', None, 'pe'),
  ('O', 'O-ring', 'NBR', None, 'o'),
  ('VK', 'Uszczelka statyczna', 'TPU', None, 'vk'),
  ('DU', 'Uszczelka statyczna', 'TPU', None, 'du'),
]
