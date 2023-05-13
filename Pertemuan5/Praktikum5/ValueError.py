# 7
umur = "17 tahun"

try:
    umur_angka = int(umur)
except ValueError:
    print("Error: Umur harus berupa angka!")