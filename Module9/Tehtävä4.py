import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeudenmuutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeudenmuutos
        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus <= 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, edetty_aika):
        matka = self.nykyinen_nopeus * edetty_aika
        self.kuljettu_matka += matka

def autot(Auto):
    Autot = []
    for i in range(10):
        rekisteritunnus = f"ABC-{i+1}"
        huippunopeus = random.randint(100,200)
        auto = Auto(rekisteritunnus, huippunopeus)
        Autot.append(auto)
    return Autot
def main():
    autot_lista = autot(Auto)
    kilpailu_jatkuu = True
    tunnit = 0
    while kilpailu_jatkuu:
        tunnit += 1
        print(tunnit)
        for auto in autot_lista:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)
            print(f"{auto.rekisteritunnus} {auto.nykyinen_nopeus} {auto.kuljettu_matka}")
            if auto.kuljettu_matka >= 10000:
                kilpailu_jatkuu = False
                break
    for auto in autot_lista:
        print(f"""Auton rekisteritunnus: {auto.rekisteritunnus},
          Huippunopeus: {auto.huippunopeus:.0f} 
          huippunopeus: {auto.huippunopeus:.0f} 
          tämänhetkinen nopeus: {auto.nykyinen_nopeus} 
          kuljettu matka: {auto.kuljettu_matka} """)

main()