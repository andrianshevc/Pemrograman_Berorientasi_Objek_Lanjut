class Customer:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def membeli(self):
        print(self.nama, "sedang membeli paket di shopee ")

class Kurir:
    def __init__(self, nama, kurir):
        self.nama = nama
        self.kurir = kurir
    def mengantar(self):
        print(self.nama, "sedang mengantar paket ke pembeli")

class CustomerKurir(Customer, Kurir):
    def __init__(self, nama, nim, kurir):
        Customer.__init__(self, nama, nim)
        Kurir.__init__(self, nama, kurir)
    def membayar(self):
        print(self.nama, "sedang membayar paket ke kurir cod")
mhs_kurir = CustomerKurir("Sheva", "190001", "Programmer")
mhs_kurir.membeli() 
mhs_kurir.mengantar() 
mhs_kurir.membayar() 