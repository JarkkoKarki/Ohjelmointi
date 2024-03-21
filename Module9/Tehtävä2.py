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

auto = Auto("AVK-142", 120)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton nopeus: {auto.nykyinen_nopeus}")
auto.kiihdytä(-200)
print(f"Auton nopeus: {auto.nykyinen_nopeus}")
