import random
N = n = 0
luku = int(input("Syötä arvottavien pisteiden määrä"))
while N < luku:
#arvotaan piste

    x = random.uniform(-1,1)
    y = random.uniform(-1, 1)
    N += 1

    if x * x + y * y < 1:
        n += 1

piin_likiarvo = 4 * n / N
print(f"Pisteitä yhteensä {N}, joista ympyrän sisällä {n}.")
print(f"Piin laskettu likiarvo on {piin_likiarvo}")


