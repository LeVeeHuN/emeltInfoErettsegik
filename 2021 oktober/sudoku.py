SOR_HOSSZA = 9

'''
1. FELADAT
'''
# User input bekerese
print('1. feladat')
bekertFajlNeve = input('Adja meg a bemeneti fajl nevet! ')
bekertSor = int(input('Adja meg egy sor szamat! '))
bekertOszlop = int(input('Adja meg egy oszlop szamat! '))
print()


'''
2. FELADAT
'''
# A felhasznalo altal megadott fajl beolvasasa csak olvashato modban, utf-8 kodolasban
fajl = open(bekertFajlNeve, 'r', encoding='utf-8')
beolvasottFajl = fajl.read()
fajl.close()

# A beolvasott string listava alakitasa szamonkent
feldolgozottAdatok = beolvasottFajl.split()
del(beolvasottFajl)

# A felhasznalo lepeseinek masik listaba atrakasa es eltavolitasa az elozo listabol
adatokHossza = len(feldolgozottAdatok)
FELHASZNALO_LEPESEI = []
for i in range(12):
    FELHASZNALO_LEPESEI.append(feldolgozottAdatok[adatokHossza - i - 1])
    feldolgozottAdatok.pop(adatokHossza - i - 1)

FELHASZNALO_LEPESEI.reverse()
SUDOKU_TABLAZAT = feldolgozottAdatok
del(feldolgozottAdatok)


'''
3. FELADAT
'''
print('3. feladat')

# A megadott helyen talalhato szam megkeresese
talaltErtek = int(SUDOKU_TABLAZAT[((bekertSor - 1) * 9) + (bekertOszlop - 1)])
if talaltErtek == 0:
    print('Az adott helyet meg nem toltottek ki.')
else:
    print(f'Az adott helyen szereplo szam: {talaltErtek}')

# A megadott hely resztablajanak megkeresese
def resztabla_helymeghatarozo(szam):
    if szam / 3 <= 1:
        return 1
    elif szam / 3 <= 2:
        return 2
    else:
        return 3

resztablaOszlop = resztabla_helymeghatarozo(bekertOszlop)
resztablaSor = resztabla_helymeghatarozo(bekertSor)
resztablaSorszama = resztablaOszlop * resztablaSor
print(f'A hely a(z) {resztablaSorszama} resztablahoz tartozik.\n')


'''
4. FELADAT
'''
uresHelyekAranya = (SUDOKU_TABLAZAT.count('0') / len(SUDOKU_TABLAZAT) * 100).__round__(1)
print(f'4. feladat\nAz ures helyek aranya: {uresHelyekAranya}%\n')


'''
5. feladat
'''
# A listaban talalhato ertekek atalakitasa stringbol integerre
for i in range(len(FELHASZNALO_LEPESEI)):
    FELHASZNALO_LEPESEI[i] = int(FELHASZNALO_LEPESEI[i])

# A felhasznalo lepeseinek listaba rendezese
for i in range(int(len(FELHASZNALO_LEPESEI) / 3)):
    z = []
    x = 0
    while x <= 2:
        z.append(FELHASZNALO_LEPESEI[0])
        FELHASZNALO_LEPESEI.pop(0)
        x += 1
    FELHASZNALO_LEPESEI.append(z)

# szam, sor, oszlop
print('5. feladat')
for lepesek in FELHASZNALO_LEPESEI:
    szam = lepesek[0]
    sor = lepesek[1]
    oszlop = lepesek[2]
    print(f'A kivalasztott sor: {sor} oszlop: {oszlop} a szam: {szam}')

    helyErteke = int(SUDOKU_TABLAZAT[((sor - 1) * 9) + (oszlop - 1)])
    if helyErteke != 0:
        print('A helyet mar kitoltottek.\n')
    else:
        helyIndex = (sor - 1) * 9 + (oszlop - 1)
        sorElejeIndex = helyIndex - oszlop - 1
        vanSzam = False
        for i in range(9):
            if int(SUDOKU_TABLAZAT[sorElejeIndex + i]) == szam:
                vanSzam = True
        if vanSzam:
            print('Az adott sorban mar szerepel a szam.\n')
        else:
            oszlopEleje = helyIndex - (sor - 1) * 9
            vanSzam = False
            for i in range(9):
                if int(SUDOKU_TABLAZAT[oszlopEleje + i * 9]) == szam:
                    vanSzam = True
            if vanSzam:
                print('Az adott oszlopban mar szerepel a szam.\n')
            else:
                # Resztablazatos szopas
                miResztablank = resztabla_helymeghatarozo(sor) * resztabla_helymeghatarozo(oszlop)
                miResztablankElemei = []
                for i in range(len(SUDOKU_TABLAZAT)):
                    jelenlegiOszlop = i % 9
                    jelenlegiSor = i // 9
                    jelenlegiResztabla = resztabla_helymeghatarozo(jelenlegiSor) * resztabla_helymeghatarozo(jelenlegiOszlop)
                    if jelenlegiResztabla == miResztablank:
                        miResztablankElemei.append(int(SUDOKU_TABLAZAT[i]))
                print(f'A szamunk: {szam}\nResztabla szamai: {miResztablankElemei}')
                if szam in miResztablankElemei:
                    print('Az adott resztablazatban mar szerepel a szam.\n')
                else:
                    print('A lepes megteheto.\n')
