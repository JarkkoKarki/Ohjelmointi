# Määritetään käyttäjätunnus ja salasana
käyttäjätunnus = "python"
salasana = "rules"

# Määritetään yritykset ja maksimi yritysten määrä
total_tries = 5
tries = 0

# While loop joka toistuu maksimi yritysten verran
while tries < total_tries:
    käyttäjä = str(input("Anna käyttäjätunnus: "))
    if käyttäjä == käyttäjätunnus:
        salis = str(input("Anna salasana: "))
        if salis == salasana:
            print("Tervetuloa")
            break

        else:
            tries +=1

    else:
        tries += 1

else:
    tries += 1
    print("Pääsy evätty")