import math

def hinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    yksikköhinta = hinta / pinta_ala
    return yksikköhinta

def main():
    #kysytään tiedot
    halkaisija1 = int(input("Anna ensimmäisen pizzan halkaisija: "))
    hinta1 = int(input("Anna ensimmäisen pizzan hinta: "))
    halkaisija2 = int(input("Anna toisen pizzan halkaisija: "))
    hinta2 = int(input("Anna toisen pizzan hinta: "))

    yksikköhinta1 = hinta(halkaisija1, hinta1)
    yksikköhinta2 = hinta(halkaisija2, hinta2)

    if yksikköhinta1 < yksikköhinta2:
        print("Pizza 1 on kannattavampi vaihtoehto")
    elif yksikköhinta2 < yksikköhinta1:
        print("Pizza 2 on kannattavampi vaihtoehto")
    else:
        print("Molemmat pizzat ovat yhtä kannattavia")
main()