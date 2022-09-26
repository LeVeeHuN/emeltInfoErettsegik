
from os import kill
from random import choice

FVI = ['F', 'I']

'''1. FELADAT'''
print(f'1. feladat\nA pénzfeldobás eredménye: {choice(FVI)}')


'''2. FELADAT'''
userTipp = input('2. feladat\nTippeljen! (F/I)= ')
dobasEredmeny = choice(FVI)
print(f'A tipp {userTipp}, a dobas eredménye {dobasEredmeny} volt.')

if userTipp is dobasEredmeny:
    print('Ön eltalálta.')
else:
    print('Ön nem találta el.')


'''3. FELADAT'''
f = open('kiserlet.txt', 'r', encoding='utf-8')

beolvasottDobasok = {'Fej': 0,
                     'Iras': 0}

nincsVege= True
while nincsVege:
    beolvasottSor = f.readline().strip()
    if beolvasottSor == 'F':
        beolvasottDobasok['Fej'] += 1
    elif beolvasottSor == 'I':
        beolvasottDobasok['Iras'] += 1
    else:
        nincsVege = False

osszesDobas = beolvasottDobasok['Fej'] + beolvasottDobasok['Iras']
print(f"3. feladat\nA kísérlet {osszesDobas} dobásból állt.")


'''4. FELADAT'''
fejRelativGyak = ((beolvasottDobasok['Fej'] / osszesDobas) * 100).__round__(2)
print(f'4.feladat\nA kísérlet során a fej relatív gyakorisága {fejRelativGyak}% volt.')


'''5. FELADAT'''
nincsVege = True
f.seek(0)
tmpList = []
kettoFej = 0
while nincsVege:
    beolvasottSor = f.readline().strip()
    if beolvasottSor in FVI:
        if beolvasottSor is 'F':
            tmpList.append('F')
        else:
            if len(tmpList) is 2:
                kettoFej += 1
                tmpList = []
            else:
                tmpList = []
    else:
        tmpList = []
        nincsVege = False

print(f'5. feladat\nA kísérlet során {kettoFej} alkalommal dobtak pontosan két fejet egymás után.')


'''6. FELADAT'''
nincsVege = True
leghosszabb = 0
hosszDict = dict()
f.seek(0)
i = 0
while nincsVege:
    i += 1
    beolvasottSor = f.readline().strip()
    if beolvasottSor in FVI:
        if beolvasottSor == 'F':
            tmpList.append('F')
        else:
            hosszDict[len(tmpList)] = i - len(tmpList)
            tmpList = []
    else:
        nincsVege = False

leghoszabbSorozat = max(hosszDict.keys())
print(f'6. feladat\nA leghosszabb tisztafej sorozat {leghoszabbSorozat} tagból áll, kezdete a(z) {hosszDict[leghoszabbSorozat]}. dobás.')

'''7. FELADAT'''
generaltDobasokLista = []
tmpStr = ''
for i in range(1000):
    for x in range(4):
        tmpStr += choice(FVI)
    generaltDobasokLista.append(tmpStr)
    tmpStr = ''

szamoloDict = {'FFFF': 0,
               'FFFI': 0}
for i in range(len(generaltDobasokLista)):
    print('Lefut')
    if generaltDobasokLista[i] == 'FFFF':
        szamoloDict['FFFF'] += 1
    elif generaltDobasokLista[i] == 'FFFI':
        szamoloDict['FFFI'] += 1

f.close()

menteni = open('dobasok.txt', 'w', encoding='utf-8')
print(f"FFFF: {szamoloDict['FFFF']}, FFFI: {szamoloDict['FFFI']}", file=menteni)
for elem in generaltDobasokLista:
    print(elem, end=' ', file=menteni)
menteni.close()
