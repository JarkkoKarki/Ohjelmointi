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
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, edetty_aika):
        matka = self.nykyinen_nopeus * edetty_aika
        self.kuljettu_matka += matka


class Kilpailu:
    def __init__(self, kilpailu_nimi, pituus_km, Autot):
        self.kilpailun_nimi = kilpailu_nimi
        self.pituus_km = pituus_km
        self.autot = Autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeudenmuutos = random.randint(-10, 15)
            auto.kiihdytä(nopeudenmuutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"""Auton rekisteritunnus: {auto.rekisteritunnus},
              Huippunopeus: {auto.huippunopeus:.0f} 
              huippunopeus: {auto.huippunopeus:.0f} 
              tämänhetkinen nopeus: {auto.nykyinen_nopeus} 
              kuljettu matka: {auto.kuljettu_matka} """)


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False


Autot = []

for i in range(10):
    rekisteritunnus = f"ABC-{i + 1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    Autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, Autot)
tunti = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()


kilpailu.tulosta_tilanne()