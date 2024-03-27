class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


    def tulosta_tiedot(self):
        return f'Julkaisun nimi: {self.nimi}'

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        return f'{super().tulosta_tiedot()}, kirjoittajan nimi: {self.kirjoittaja}, sivumäärä: {self.sivumäärä}'

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        return f'{super().tulosta_tiedot()} päätoimittajan nimi: {self.päätoimittaja}'


j1 = Lehti("Aku Ankka", "Aki Hyyppä")
j2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
print(j1.tulosta_tiedot())
print(j2.tulosta_tiedot())