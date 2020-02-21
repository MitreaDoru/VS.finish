import random
numberOfStreaks = 0
pana_la_saseH = 0
pana_la_saseT = 0
for experimentNumber in range(10000):
    numar = random.randint(0, 1)
    while numar == 0:
        pana_la_saseH += 1
        pana_la_saseT = 0
        print("H")
        break
    while numar == 1:
        pana_la_saseT += 1
        pana_la_saseH = 0
        print("T")
        break
    if pana_la_saseH == 6:
        numberOfStreaks += 1
        pana_la_saseH = 0
        pana_la_saseT = 0
    elif pana_la_saseT == 6:
        numberOfStreaks += 1
        pana_la_saseH = 0
        pana_la_saseT = 0
print('Chance of streak: %s%%'%(numberOfStreaks / 100))