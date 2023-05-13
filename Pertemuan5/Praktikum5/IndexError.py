# 5

my_list = [1, 2, 3]
try:
    # Mengakses elemen di indeks yang tidak ada
    print(my_list[3])
except IndexError:
    print("Error: Indeks diluar batas!")