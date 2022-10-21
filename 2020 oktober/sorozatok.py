import datetime
# 1. feladat
with open('lista.txt', 'r') as f: NYERSADATOK = list(f.readlines())
for i in range(len(NYERSADATOK)):
    NYERSADATOK[i] = NYERSADATOK[i].replace('\n', '')

NYERSADATOK.insert(0, None)
ADATOK, tmplist = [], []
for i in range(len(NYERSADATOK)):
    if i % 5 != 0: tmplist.append(NYERSADATOK[i])
    else:
        tmplist.append(NYERSADATOK[i])
        ADATOK.append(tmplist)
        tmplist = []
NYERSADATOK.pop(0)
ADATOK.pop(0)

for i in range(len(ADATOK)):
    ADATOK[i][3], ADATOK[i][4] = int(ADATOK[i][3]), bool(int(ADATOK[i][4]))
    ido = ADATOK[i][0].split('.')
    if ADATOK[i][0] != 'NI': ADATOK[i][0] = datetime.date(int(ido[0]), int(ido[1]), int(ido[2]))
#for a in ADATOK: print(a)

# 2. feladat
c = 0
for adat in ADATOK: c += adat.count('NI')
c = len(ADATOK) - c
print(f'2. feladat\nA listaban {c} db vetitesi datummal rendelkezo epizod van.\n')

# 3. feladat
megnezett = 0
for adat in ADATOK: megnezett += adat.count(True)
print(f'3. feladat\nA listaban levo epizodok {megnezett / len(ADATOK) * 100:.2f}%-at latta.\n')

# 4. feladat
nezettPerc = 0
for i in range(len(ADATOK)):
    if ADATOK[i][4]: nezettPerc += ADATOK[i][3]
print(f'4. feladat\nSorozatnezessel {nezettPerc // 60 // 24} napot {nezettPerc // 60 % 24} orat es {nezettPerc % 60} percet toltott.\n')

# 5. feladat
bekertDatum = input('5. feladat\nAdjon meg egy datumot! Datum= ')
ido = bekertDatum.split('.')
bekertDatum = datetime.date(int(ido[0]), int(ido[1]), int(ido[2]))
for elem in ADATOK:
    if elem[4] == False and elem[0] != 'NI' and bekertDatum >= elem[0]: print(f'{elem[2]} {elem[1]}')

# 6. feladat
def Hetnapja(ev, ho, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3: ev = ev - 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]
    return hetnapja

# 7. feladat
adottNap = input('\n7. feladat\nAdja meg a het egy napjat (peldaul cs)! Nap= ')
sorozatokAdottNap = []
for elem in ADATOK:
    if elem[0] != 'NI':
        if Hetnapja(elem[0].year, elem[0].month, elem[0].day) == adottNap:
            if elem[1] not in sorozatokAdottNap: sorozatokAdottNap.append(elem[1])
for sorozat in sorozatokAdottNap: print(sorozat)

# 7. feladat
epizodszamok = dict()
for elem in ADATOK:
    if elem[1] not in epizodszamok.keys(): epizodszamok[elem[1]] = 1
    else: epizodszamok[elem[1]] += 1

epizodidotartam = dict()
for elem in ADATOK:
    if elem[1] not in epizodidotartam.keys(): epizodidotartam[elem[1]] = elem[3]
    else: epizodidotartam[elem[1]] += elem[3]

with open('summa.txt', 'w') as f:
    for nev, ido, db in zip(list(epizodszamok.keys()), list(epizodidotartam.values()), list(epizodszamok.values())): print(f'{nev} {ido} {db}', file=f)

