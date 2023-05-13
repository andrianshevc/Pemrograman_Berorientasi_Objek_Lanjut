angka1 = 3.14
angka2 = 2

try:
    hasil = angka1 / angka2
except FloatingPointError:
    print("Error: Pembagian dengan nol pada bilangan pecahan tidak diizinkan!")