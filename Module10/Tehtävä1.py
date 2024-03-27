class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = self.alin_kerros

    def siirry_kerrokseen(self, luku):
        if luku < 0:
            for _ in range(-luku):
                self.kerros_alas()
        elif luku > 0:
            for _ in range(luku):
                self.kerros_ylös()

    def kerros_ylös(self):
        if self.ylin_kerros > self.kerros:
            self.kerros += 1

    def kerros_alas(self):
        if self.alin_kerros < self.kerros:
            self.kerros -= 1


h1 = Hissi(1, 10)
h1.siirry_kerrokseen(5)
print(h1.kerros)
h1.siirry_kerrokseen(3)
print(h1.kerros)
