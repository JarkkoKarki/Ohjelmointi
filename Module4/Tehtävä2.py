while True:
    Tuuma = int(input("Anna tuumamäärä: "))

    if Tuuma > 0:
        print(f"{Tuuma * 2.54} cm")
    else:
        print("Ohjelma lopetetaan")
        break
