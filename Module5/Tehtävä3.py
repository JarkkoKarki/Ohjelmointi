luku = int(input("Anna kokonaisluku: "))
if luku >= 2:
    luku = int(luku)

    alkuluku = True
    for n in range(2, luku):
        if luku % n == 0:
            alkuluku = False
            break
    if alkuluku:
        print(f"Luku: {luku} on alkuluku ")
    else:
        print(f"Luku: {luku} ei ole alkuluku")
else:
    print(f"Virheellinen syöte")