class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def berbunyi(self):
        print(self.nama, "berbunyi")

class Burung(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Merdu!")
kucingA = Burung("Chelsi", 2, "Merdu")
kucingA.berbunyi() 
kucingA.bersuara()