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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kWh):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti_kWh = akkukapasiteetti_kWh

class polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko_l):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko_l = bensatankin_koko_l


class Kilpailu:
    def __init__(self, kilpailu_nimi, pituus_km, Autot):
        self.kilpailun_nimi = kilpailu_nimi
        self.pituus_km = pituus_km
        self.autot = Autot
        self.tunnit = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeudenmuutos = random.randint(-10, 15)
            auto.kiihdytä(nopeudenmuutos)
            auto.kulje(1)
            print(f"{auto.rekisteritunnus} {auto.nykyinen_nopeus} {auto.kuljettu_matka}")


    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"""Auton rekisteritunnus: {auto.rekisteritunnus},
              Huippunopeus: {auto.huippunopeus:.0f} 
              huippunopeus: {auto.huippunopeus:.0f} 
              tämänhetkinen nopeus: {auto.nykyinen_nopeus} 
              kuljettu matka: {auto.kuljettu_matka} """)

    def kilpailu_ohi(self):
        self.tunnit += 1
        if self.tunnit % 3 == 0:
            return True
        return False


Autot = [Sähköauto("ABC-15", 180, 52.5), polttomoottoriauto("ACD-123", 165, 32.3)]

kilpailu = Kilpailu("Suuri romuralli", 1000, Autot)

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()

kilpailu.tulosta_tilanne()