def parilliset(numerot):
    #lisätään uusi tyhjä lista, millä ei ole mitään tekemistä alkup. kanssa
    parilliset_numerot = []
    for num in range(len(numerot)-1):
        if numerot[num] % 2 == 0:
            #lisätään aina uuteen listaan, jos se on parillinen
            parilliset_numerot.append(numerot[num])
    return parilliset_numerot

#listoista pitää poistaa 1
numerot = [1,2,3,4,5,6,7,8,9,10]
parilliset_numerot = parilliset(numerot)
print(f"Alkuperäiset luvut: {numerot}, ja parilliset luvut: {parilliset_numerot}")