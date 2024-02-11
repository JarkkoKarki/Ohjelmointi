lentoasemat = {}
def main():
    while True:
        toiminto = input("Haluatko syöttää lentokentän / Hakea lentokentän / Lopettaa ohjelman: 'S' / 'H' / 'L' ")
        if toiminto == 'S':
            koodi = input("Syötä ICAO-koodi: ")
            nimi = input("Syötä lentokentän nimi: ")
            lentoasemat[koodi] = nimi
        elif toiminto == 'H':
            koodi = input(" Syötä ICAO-koodi: ")
            if koodi in lentoasemat:
                print(lentoasemat[koodi])
        elif toiminto == 'L':
            print("Ohjelma lopetetaan")
            break
        else:
            print("Väärä syöte")


main()