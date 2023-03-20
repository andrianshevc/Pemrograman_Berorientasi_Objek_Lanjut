class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")

class Pribadi:
    def __init__(self, hobi, alamat):
        self.hobi = hobi
        self.alamat = alamat
    def display_info(self):
        print(f"Hobi: {self.hobi}")
        print(f"Alamat: {self.alamat}")
class PribadiPekerja(Orang, Pekerja, Pribadi):
    def __init__(self, nama, umur, pekerjaan, gaji, hobi, alamat):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Pribadi.__init__(self, hobi, alamat)
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Hobi: {self.hobi}")
        print(f"Alamat: {self.alamat}")
# contoh penggunaan
pribadi_pekerjaC = PribadiPekerja("Sheva", 19, "Digital Marketing", "20 Juta", "Bermain Bola", "Arjawinangun")
pribadi_pekerjaC.display_info()
