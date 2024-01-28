import random
# Kone arpoo satunnaisen luvun
oikea_luku = random.randint(1,10)

# While loop, jossa kysytään numeroa ja verrataan sitä oikeaan lukuun

while True:
    arvaus = int(input("Arvaa oikea luku väliltä 1-10: "))
    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print(f"Oikein")
        break