


class House:
    """ House class """

    def __init__(self,nazwa:str,okna:int,dach:str,drzwi:int,sciany:int):
        self.nazwa = nazwa
        self.okna = okna
        self.dach = dach
        self.drzwi = drzwi
        self.sciany = sciany

    def powiedz_dziendobry(self,imie:str):
        return f"Dzien dzien dobry sąsiedzie {imie}"

    def otworz_drzwi(self):
        print(f"Owieram drzwi na {self.drzwi}")

    def otworz_okno(self):
        print(f"Owieram okno na {self.okna}")

    def wyjdz_przez_drzwi(self):
        print(f"Owieram drzwi na {self.drzwi}")


domek = House(nazwa="Kuba",
              okna=5,
              dach="Spadzisty",
              drzwi=4,
              sciany=5)

print(domek.nazwa)
print(domek.okna)
print(domek.dach)
print(domek.drzwi)
domek.otworz_okno()
domek.otworz_drzwi()
domek.wyjdz_przez_drzwi()
print(domek.powiedz_dziendobry(imie="Kuba"))
