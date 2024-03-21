class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("AVK-142", 120)
print(f"""Auton rekisteritunnus: {auto.rekisteritunnus},
      Huippunopeus: {auto.huippunopeus:10.0f} 
      huippunopeus: {auto.huippunopeus:10.0f} 
      tämänhetkinen nopeus: 
      {auto.nykyinen_nopeus} 
      kuljettu matka: 
      {auto.kuljettu_matka} """)
