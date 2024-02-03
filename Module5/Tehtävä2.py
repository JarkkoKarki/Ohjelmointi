lista = []
while True:
    luku = input("Anna numero")
    if luku == "":
        break

    else:
        numero = int(luku)
        lista.append(numero)

if len(lista) > 0:
    viisilukua = sorted(lista, reverse=True,)[:5]
    print(f"Viisi suurinta lukua: {viisilukua}")
