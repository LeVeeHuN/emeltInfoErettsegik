# 1. feladat
with open('melyseg.txt', 'r') as f:
    ADATOK = f.read().split()
print(f'1. feladat\nA fajl adatainak szama: {len(ADATOK)}\n')

# 2. feladat
bekertTavolsag = int(input('2. feladat\nAdjon meg egy tavolsagerteket! '))
print(f'Ezen a helyen a felszin {ADATOK[bekertTavolsag - 1]} meter melyen van.\n')

# 3. feladat
print(f'3. feladat\nAz erintetlen terulet aranya {ADATOK.count("0") / len(ADATOK) * 100:.2f}%.\n')

# 4. feladat
tmp, godrok, legalabbEgy = [], [], False
for melyseg in ADATOK:
    if melyseg != '0':
        tmp.append(melyseg)
        legalabbEgy = True
    elif melyseg == '0' and legalabbEgy:
        legalabbEgy = False
        godrok.append(tmp)
        tmp = []

with open('godrok.txt', 'w') as f:
    for godor in godrok:
        for melyseg in godor:
            print(melyseg, end=' ', file=f)
        print(file=f)

# 5. feladat
print(f'5. feladat\nA godrok szama: {len(godrok)}\n')

# 6. feladat
print('6. feladat')
bekertIndex = bekertTavolsag - 1
if ADATOK[bekertIndex] == '0':
    print('Az adott helyen nincs godor.')
else:
    nincsGodor = True
    i = bekertIndex
    while nincsGodor:
        if ADATOK[i] == '0':
            nincsGodor = False
            kezdopont = i + 2
        else:
            i -= 1
    nincsGodor = True
    i = bekertIndex
    while nincsGodor:
        if ADATOK[i] == '0':
            nincsGodor = False
            vegpont = i
        else:
            i += 1
    print(f'a)\nA godor kezdete: {kezdopont} meter, a godor vege: {vegpont} meter.')
    bekertGodor = []
    for i in range(vegpont - kezdopont + 1):
        bekertGodor.append(int(ADATOK[kezdopont - 1 + i]))

    melysegek = []
    for melyseg in bekertGodor:
        if melyseg not in melysegek:
           melysegek.append(melyseg)

    if len(melysegek) <= 1:
        print('b)\nNem melyul folyamatosan.')
    else:
        legmelyebbIndex = bekertGodor.index(max(bekertGodor))
        godorBal, godorJobb = [], list(bekertGodor)
        for i in range(legmelyebbIndex):
            godorBal.append(godorJobb[0])
            godorJobb.pop(0)
        godorBalSorted = list(godorBal)
        godorBalSorted.sort()
        godorJobbSorted = list(godorJobb)
        godorJobbSorted.sort()
        godorJobbSorted.reverse()
        if godorBalSorted == godorBal and godorJobbSorted == godorJobb:
            print('b)\nFolyamatosan melyul.')
        else:
            print('b)\nNem melyul folyamatosan.')
    print(f'c)\nA legnagyobb melysege {max(bekertGodor)} meter.')

    SZELESSEG, terfogat = 10, 0
    for melyseg in bekertGodor:
        terfogat += SZELESSEG * melyseg
    print(f'd)\nA terfogata {terfogat} m^3.')

    vizmennyiseg = 0
    for melyseg in bekertGodor:
        if melyseg > 1:
            vizmennyiseg += SZELESSEG * (melyseg - 1)
    print(f'e)\nA vizmennyiseg {vizmennyiseg} m^3.')
