def hitung_luas_segitiga(alas, tinggi):
    assert alas > 0, "Alas harus lebih besar dari 0"
    assert tinggi > 0, "Tinggi harus lebih besar dari 0"
    luas = 0.5 * alas * tinggi
    return luas

# Contoh penggunaan fungsi hitung_luas_segitiga
alas = 5
tinggi = 0

try:
    hasil = hitung_luas_segitiga(alas, tinggi)
    print("Luas segitiga:", hasil)
except AssertionError as e:
    print("Error:", e)