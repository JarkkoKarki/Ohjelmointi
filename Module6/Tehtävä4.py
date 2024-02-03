def laske_summa(lista):
    return sum(lista)

def main():
    lista = []
    while True:
        luku = input("Anna kokonaisluku (tyhjä lopettaa): ")
        if luku == "":
            print(f"Syötetyt luvut: {lista}")
            summa = laske_summa(lista)
            print(f"Summa: {summa}")
            break

        else:
            luku = int(luku)
            lista.append(luku)






main()