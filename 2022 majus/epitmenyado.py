sorok = []
arnmkent = []
adatok = []
fizetendoAdo = [0,0,0]
epuletekSzama = [0,0,0]

#ADATOK BEOLVASÁSA
with open('utca.txt', 'r', encoding='utf-8') as f:
    for sor in f:
        sorok.append(sor)

#ADATOK FELDOLGOZÁSA

#négyzetméterenkénti ár listába mentése
#és eltávolítása a nagy listából
#és a maradék sorok listába rakása soronként
arnmkent = sorok[0].split()
sorok.pop(0)

for adat in sorok:
    adatok.append(adat.split())


#2. FELADAT
print(f'2. feladat. A mintában {len(sorok)} telek szerepel.')


#3. FELADAT
adoszam = input('3. feladat. Egy tulajdonos adószáma: ')
szereplesek = 0

for adat in adatok:
    if adoszam == adat[0]:
        szereplesek += 1
        print(f'{adat[1]} utca {adat[2]}')

if szereplesek == 0:
    print('Nem szerepel az adatállományban.')


#4. FELADAT
def ado(adosav, alapterulet):
    if adosav == 'A':
        kukac = int(arnmkent[0])*int(alapterulet)
    elif adosav == 'B':
        kukac = int(arnmkent[1])*int(alapterulet)
    else:
        kukac = int(arnmkent[2])*int(alapterulet)
    
    if kukac < 10000:
        return 0
    else:
        return kukac


#5. FELADAT
for adat in adatok:
    if adat[3] == 'A':
        epuletekSzama[0] += 1
        fizetendoAdo[0] += ado(adat[3], adat[4])
    elif adat[3] == 'B':
        epuletekSzama[1] += 1
        fizetendoAdo[1] += ado(adat[3], adat[4])
    else:
        epuletekSzama[2] += 1
        fizetendoAdo[2] += ado(adat[3], adat[4])

print(f'A sávba {epuletekSzama[0]} telek esik, az adó {fizetendoAdo[0]} Ft.')
print(f'B sávba {epuletekSzama[1]} telek esik, az adó {fizetendoAdo[1]} Ft.')
print(f'C sávba {epuletekSzama[2]} telek esik, az adó {fizetendoAdo[2]} Ft.')


#6. FELADAT
adatokDict = dict()

for adat in adatok:
    utca = adat[1]
    if utca not in adatokDict:
        adatokDict[utca] = adat[3]
    else:
        pass

    adosav = adat[3]
    if adosav not in adatokDict[utca]:
        adatokDict[utca] += adosav
    else:
        pass

for utca in adatokDict:
    if len(adatokDict[utca]) > 1:
        print(utca)


#7. feladat
tulajdonosokDict = dict()

for adat in adatok:
    adoszam = adat[0]
    if adoszam not in tulajdonosokDict:
        tulajdonosokDict[adoszam] = ado(adat[3], adat[4])
    else:
        tulajdonosokDict[adoszam] += ado(adat[3], adat[4])

        
f = open('fizetendo.txt', 'w', encoding='utf-8')
for t in tulajdonosokDict:
    print(f'{t} {tulajdonosokDict[t]}', file=f)
f.close()
    
    
