def hitung_luas():
    panjang = 10
    lebar = 5
    luas = panjang * lebar
    return luas

try:
    hasil = hitung_luas()
    print("Hasil: ", hasil)
except TabError:
    print("Error: Terdapat kesalahan indentasi menggunakan tab!")