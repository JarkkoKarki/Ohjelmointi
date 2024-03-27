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
        else:
            pass

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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_nro, kohde_kerros):
        hissi = self.hissit[hissin_nro]
        hissi.siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.kerros = self.alin_kerros



t1 = Talo(1, 10, 3)
t1.aja_hissiä(2, 5)
print(t1.hissit[2].kerros)
t1.palohälytys()
print(t1.hissit[2].kerros)
