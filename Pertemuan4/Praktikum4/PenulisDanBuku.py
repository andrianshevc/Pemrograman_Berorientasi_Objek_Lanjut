class Penulis:
    def __init__(self, nama_penulis):
        self.nama_penulis = nama_penulis
        self.karyas = []

    def tambah_karya(self, judul, tahun_terbit):
        karya = Buku(judul, tahun_terbit)
        self.karyas.append(karya)

class Buku:
    def __init__(self, judul, tahun_terbit):
        self.judul = judul
        self.tahun_terbit = tahun_terbit

# membuat objek penulis
john_doe = Penulis("John Doe")

# menambahkan buku ke daftar karya penulis
john_doe.tambah_karya("The Art of Programming", 2020)
john_doe.tambah_karya("Data Structures and Algorithms", 2021)

# mencetak informasi karya penulis
for karya in john_doe.karyas:
    print(karya.judul, karya.tahun_terbit)