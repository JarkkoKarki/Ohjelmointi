print("Kerro kolme kokonaislukua, joista haluat summan, tulon ja keskiarvon")
ensimmäinen = int(input("Ensimmäinen kokonaisluku:\n"))
toinen = int(input("Toinen kokonaisluku:\n"))
kolmas = int(input("Kolmas kokonaisluku:\n"))
tulo = ensimmäinen * toinen * kolmas
summa = ensimmäinen + toinen + kolmas
keskiarvo = summa / 3
print(f"Tulo: {tulo}, summa: {summa}, keskiarvo: {keskiarvo}")