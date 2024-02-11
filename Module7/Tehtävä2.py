joukko = set()
print("(Tyhjä merkkijono lopettaa ohjelman)")
while True:
    nimi = input("Syötä nimi: ")
    if nimi in joukko:
        print("Aiemmin syötetty nimi")
    elif nimi == "":
        for i in joukko:
            print(i)
    else:
        joukko.add(nimi)
        print("nimeä ei ole syötetty aikaisemmin")
