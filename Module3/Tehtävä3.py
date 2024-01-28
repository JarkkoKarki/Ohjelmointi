Sukupuoli = str(input('Kerro biologinen sukupuoli "M" / "N": '))
hemoglobiini = int(input("Kerro hemoglobiini arvo (g/l): "))
if Sukupuoli == "N" :
    if hemoglobiini < 117:
        print("Hemoglobiini arvo on alhainen.")
    elif hemoglobiini >= 117 and hemoglobiini <= 175:
        print("Hemoglobiini arvo on normaali")
    elif hemoglobiini > 175:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Virheellinen sukupuoli ")

if Sukupuoli == "M" :
    if hemoglobiini < 134:
        print("Hemoglobiini arvo on alhainen.")
    elif hemoglobiini >= 134 and hemoglobiini <= 195:
        print("Hemoglobiini arvo on normaali")
    elif hemoglobiini > 195:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Virheellinen sukupuoli ")