# Alustetaan arvot
max_number = None
min_number = None

# While loop
while True:

    luku = input("Syötä luku \n(enter lopettaa ohjelman) ")
    # Mikäli tyhjä syöttö ohjelma lopetetaan
    if luku == "":
        print(f"Suurin luku {max_number} ja pienin luku {min_number}")
        break
    else:
        current_number = int(luku)
        if max_number is None or current_number > max_number:
            max_number = current_number
        if min_number is None or current_number < min_number:
            min_number = current_number