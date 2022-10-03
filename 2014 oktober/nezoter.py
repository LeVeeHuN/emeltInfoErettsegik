
from itertools import count
from operator import indexOf


foglaltsag = []
kategoria = []

f = open('foglaltsag.txt', 'r').readlines()
for sor in f:
    foglaltsag.append(sor.strip())

f = open('kategoria.txt', 'r')
for sor in f:
    kategoria.append(sor.strip())


# 2. feladat
print('2. feladat')

bekertSor = int(input('Adja meg egy sor számát: '))
bekertSzek = int(input('Adja meg egy szék számát: '))

if foglaltsag[bekertSor - 1][bekertSzek - 1] == 'x':
    print('Az adott hely már foglalt.')
else:
    print('Az adott hely szabad.')


# 3. feladat
print('3. feladat')

eladottJegyek = 0
for sor in foglaltsag:
    eladottJegyek += sor.count('x')

print(f'Az előadásra eddig {eladottJegyek} jegyet adtak el, ez a nézőtér {(eladottJegyek / (len(foglaltsag) * len(foglaltsag[0])) * 100):.0f}%-a.')


# 4. feladat
print('4. feladat')

eladasKatSzerint = dict()
jelenlegiSorIndexe = 0
jelenlegiHelyIndexe = 0

for sor in foglaltsag:
    for hely in sor:
        if hely == 'x':
            jelenlegiHelyKat = kategoria[jelenlegiSorIndexe][jelenlegiHelyIndexe]
            if jelenlegiHelyKat not in eladasKatSzerint:
                eladasKatSzerint[jelenlegiHelyKat] = 1
            else:
                eladasKatSzerint[jelenlegiHelyKat] += 1
        jelenlegiHelyIndexe += 1
    jelenlegiHelyIndexe = 0
    jelenlegiSorIndexe += 1

legtobbEladottJegyKatIndexe = indexOf(eladasKatSzerint.values(), max(eladasKatSzerint.values()))
legtobbetEladottJegyKat = list(eladasKatSzerint.keys())[legtobbEladottJegyKatIndexe]
print(f'A legtöbb jegyet a(z) {legtobbetEladottJegyKat}. árkategóriában értékesítették.')


# 5. feladat
print('5. feladat')
jegyarak = {'1': 5000,
            '2': 4000,
            '3': 3000,
            '4': 2000,
            '5': 1500}

befolytOsszeg = 0

for key, value in eladasKatSzerint.items():
    befolytOsszeg += value * jegyarak[key]

print(f'A színház bevétele a pillanatnyilag eladott jegyek alapján: {befolytOsszeg}')


# 6. feladat
print('6. feladat')

egyedulalloHelyek = 0
hozzaadando = False

for sor in foglaltsag:
    for i in range(len(sor)):
        try:
            if sor[i] == 'o' and sor[i + 1] == 'o':
                egyedulalloHelyek += 1
                hozzaadando = True
            else:
                if hozzaadando:
                    egyedulalloHelyek += 1
                    hozzaadando = False
        except:
            if hozzaadando:
                egyedulalloHelyek += 1
                hozzaadando = False

osszesUresHely = 0
for sor in foglaltsag:
    osszesUresHely += sor.count('o')
print(f'Egyedulallo helyek: {osszesUresHely - egyedulalloHelyek}')


# 7. feladat
kimenetiFajl = open('szabad.txt', 'w')

sorStr = ''
sorIndexe = 0
for jSor in range(len(foglaltsag)):
    for jHely in range(len(foglaltsag[jSor])):
        if foglaltsag[jSor][jHely] == 'x':
            sorStr += 'x'
        else:
            sorStr += f'{kategoria[jSor][jHely]}'
    print(sorStr, file=kimenetiFajl)
    sorStr = ''
kimenetiFajl.close()
