leiviskä = float(input("Anna leiviskät. "))
naula = float(input("Anna naulat. "))
luoti = float(input("Anna luodit. "))
#Lasketaan luotien määrä
naulat_yhteensä = (leiviskä * 20)
leiviskät_yhteensä = (naulat_yhteensä + naula) * 32
luodit_yhteensä = (leiviskät_yhteensä + luoti) * 13.3
#lasketaan massa
luodit_yhteensä_kg = int(luodit_yhteensä / 1000)
luodit_yhteensä_g = float(luodit_yhteensä % 1000)
print(f"Massa nykymittojen mukaan:\n{luodit_yhteensä_kg} kilogrammaa ja {luodit_yhteensä_g:3.2f} grammaa.")