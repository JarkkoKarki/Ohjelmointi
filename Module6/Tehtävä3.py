def galloonat(galloona_maara):
    litrat = galloona_maara * 3.785
    return litrat

def main():
    while True:
        galloona = int(input("Syötä bensiinin määrä gallonoina \n(negatiivinen luku lopettaa): "))
        if galloona < 0:
            print("Ohjelma lopetetaan")
            break
        litra = galloonat(galloona)
        print(f"Galloonat litroina on: {litra:.2f} l")

main()