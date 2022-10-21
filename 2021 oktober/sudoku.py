# 1. feladat
from itertools import count


print('1. feladat')
bemenetiFajl = input('Adja meg a bementi fajl nevet! ')
felhasznaloSor = int(input('Adja meg egy sor szamat! '))
felhasznaloOszlop = int(input('Adja meg egy oszlop szamat! '))


# 2. feladat
TABLAZAT = []
LEPESEK = []

f = open(bemenetiFajl).read()
BEOLVASOTT_ADATOK = f.strip().splitlines()

for i in range(13):
    if i < 9:
        TABLAZAT.append(BEOLVASOTT_ADATOK[i].split())
    else:
        LEPESEK.append(BEOLVASOTT_ADATOK[i].split())


# 3. feladat
print('\n3. feladat')
keresettMezoErteke = TABLAZAT[felhasznaloSor - 1][felhasznaloOszlop - 1]
if int(keresettMezoErteke) != 0:
    print(f'Az adott helyen szereplo szam: {keresettMezoErteke}')
    resztabla = ((felhasznaloOszlop - 1) // 3 + ((felhasznaloSor - 1) // 3) * 3) + 1
    print(f'A hely a(z) {resztabla} resztablahoz tartozik.')
else:
    print('Az adott helyet meg nem toltottek ki.')


# 4. feladat
print('\n4. feladat')
osszesHely = 0
uresHely = 0

for sor in TABLAZAT:
    osszesHely += len(sor)
    uresHely += sor.count('0')

print(f'Az ures helyek aranya: {uresHely / osszesHely * 100:.1f}%')


# 5. feladat
print('\n5. feladat')

def ertekAzOszlopban(ertek, oszlop):
    for sor in TABLAZAT:
        if sor[oszlop - 1] == str(ertek):
            return True
    return False

def resztablaHelper(resztabla):
    resztablaErtekei = []
    for sor in range(len(TABLAZAT)):
        for oszlop in range(len(TABLAZAT[sor])):
            jelenlegiResztabla =( oszlop // 3) + ((sor // 3) * 3) + 1
            if jelenlegiResztabla == resztabla:
                resztablaErtekei.append(TABLAZAT[sor][oszlop])
    return resztablaErtekei

def ertekAResztablaban(ertek, sor, oszlop):
    resztabla = ((oszlop - 1) // 3 + ((sor - 1) // 3) * 3) + 1
    if str(ertek) in resztablaHelper(resztabla):
        return True
    else:
        return False


for lepes in LEPESEK:
    ertek, sor, oszlop = int(lepes[0]), int(lepes[1]), int(lepes[2])

    resp = str()
    if TABLAZAT[sor - 1][oszlop - 1] != '0':
        resp = 'A helyet mar kitoltottek.'
    elif ertek in TABLAZAT[sor - 1]:
        resp = 'Az adott sorban mar szerepel a szam.'
    elif ertekAzOszlopban(ertek, oszlop):
        resp = 'Az adott oszlopban mar szerepel a szam.'
    elif ertekAResztablaban(ertek, sor, oszlop):
        resp = 'Az adott resztablazatban mar szerepel a szam.'
    else:
        resp = 'A lepes megteheto.'
    
    print(f'A kivalasztott sor: {sor} oszlop: {oszlop} a szam: {ertek}')
    print(resp, end='\n\n')
