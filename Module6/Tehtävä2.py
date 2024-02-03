import random


def noppa(tahkot):
    silmaluku = random.randint(1, tahkot)
    return silmaluku


tahkojenmaara = int(input("Syötä tahkojen määrä: "))
maksimisilmaluku = int(input("Syötä nopan maksimisilmäluku: "))
while True:
    heitto = noppa(tahkojenmaara)
    print("Nopan silmaluku:", heitto)
    if heitto == maksimisilmaluku:
        break