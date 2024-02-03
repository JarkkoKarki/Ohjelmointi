import random
summa = 0
luku = int(input(f"montako arpakuutiota heitetään?: "))
for n in range(luku):
    silmaluku = random.randint(1,6)
    summa += silmaluku
    print(f"{silmaluku}")

print(f"Kaikkien silmälukujen summa = {summa}")