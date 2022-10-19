

# 1.
from operator import indexOf


f = open('tavirathu13.txt', 'r', encoding='utf-8')
beolvasottAdatok = f.read()
sorok = beolvasottAdatok.splitlines()
feldolgozottSorok = []

for i in range(len(sorok)):
    tmpList = sorok[i].split()
    feldolgozottSorok.append(tmpList)
    


# 2.
bekertKod = input('2. feladat\nAdja meg egy telepules kodjat! Telepules: ')
telepulesMeresei = []

for telepules in feldolgozottSorok:
    if bekertKod in telepules:
        telepulesMeresei.append(telepules[1])

legkesobbiMeres = max(telepulesMeresei)
print(f'Az utolso meresi adat a megadott telepulesrol {legkesobbiMeres[:2]}:{legkesobbiMeres[2] + legkesobbiMeres[3]}-kor erkezett.')



# 3.
homersekletek = []

for sor in feldolgozottSorok:
    homersekletek.append(sor[3])

legnHomKod = homersekletek.index(max(homersekletek))
legkHomKod = homersekletek.index(min(homersekletek))
sorK, sorN = feldolgozottSorok[legkHomKod], feldolgozottSorok[legnHomKod]
idoK, idoN = sorK[1], sorN[1]
oraK, oraN = idoK[0] + idoK[1], idoN[0] + idoN[1]
percK, percN = idoK[2] + idoK[3], idoN[2] + idoN[3]

legalacsonyabbString = f'A legalacsonyabb homerseklet: {feldolgozottSorok[legkHomKod][0]} {oraK}:{percK} {feldolgozottSorok[legkHomKod][3]} fok.'
legnagyobbString = f'A legmagasabb homerseklet: {feldolgozottSorok[legnHomKod][0]} {oraN}:{percN} {feldolgozottSorok[legnHomKod][3]} fok.'
print(f'3. feladat\n{legalacsonyabbString}\n{legnagyobbString}')



# 4.
szelcsendek = []

for sor in feldolgozottSorok:
    if sor[2] == '00000':
        tmpList = []
        tmpList.append(sor[0])
        tmpList.append(f'{sor[1][:2]}:{sor[1][2]}{sor[1][3]}')
        szelcsendek.append(tmpList)

print('4. feladat')
if len(szelcsendek) == 0:
    print('Nem volt szelcsend a meresek idejen')
else:
    for eset in szelcsendek:
        print(eset[0] + ' ' + eset[1])



# 5.
telepulesek = []
feldolgozottSorok2 = feldolgozottSorok
popoltElemek = 0
i = 0
telepulesIndex = dict()
nincsKesz = True

while nincsKesz:
    try:
        telepulesKodja = feldolgozottSorok2[i - popoltElemek][0]
        if telepulesKodja not in telepulesIndex.keys():
            telepulesIndex[telepulesKodja] = len(telepulesIndex)
            telepulesek.append(list())
        
        tmpList = []
        tmpList.append(feldolgozottSorok2[i - popoltElemek][1])
        tmpList.append(feldolgozottSorok2[i - popoltElemek][3])
        tmpList.append(feldolgozottSorok2[i - popoltElemek][2])
        telepulesIndexe = telepulesIndex[telepulesKodja]
        telepulesek[telepulesIndexe].append(tmpList)

        i += 1
    except:
        nincsKesz = False
        break

# a)
print('5. feladat')
idopontok = [['0', '1'], ['0', '7'], ['1', '3'], ['1', '9']]

for varosKodja in telepulesIndex.keys():
    homersekletek = []
    kozHomErtekek = []
    for varos in telepulesek[telepulesIndex[varosKodja]]:
        
        homersekletek.append(varos[1])

        for idopont in idopontok:
            if varos[0][0] == idopont[0] and varos[0][1] == idopont[1]:
                kozHomErtekek.append(varos[1])

    if len(kozHomErtekek) > len(idopontok):
        osszeg = 0
        for ertek in kozHomErtekek:
            osszeg += int(ertek)
        kozephomerseklet = round(osszeg / len(kozHomErtekek))
        print(f'{varosKodja} Kozephomerseklet: {kozephomerseklet}; ', end='')
    else:
        print(f'{varosKodja} NA; ', end='')

    minHom = int(min(homersekletek))
    maxHom = int(max(homersekletek))
    homIngadozas = maxHom - minHom
    print(f'Homerseklet-ingadozas: {homIngadozas}')

    fajlMenteni = open(f'{varosKodja}.txt', 'w', encoding='utf-8')
    print(varosKodja, file=fajlMenteni)
    for telepules in telepulesek[telepulesIndex[varosKodja]]:
        ora = telepules[0][0] + telepules[0][1]
        perc = telepules[0][2] + telepules[0][3]
        ido = ora + ':' + perc
        szelerosseg = int(telepules[2][3] + telepules[2][4])

        print(f'{ido} {szelerosseg * "#"}', file=fajlMenteni)
print('6. feladat\nA fajlok elkeszultek.')
