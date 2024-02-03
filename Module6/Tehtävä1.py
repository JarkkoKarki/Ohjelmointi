import random


def noppa():
    silmäluku = random.randint(1,6)
    print(silmäluku)
    return silmäluku

while True:
    if noppa() == 6:
        break