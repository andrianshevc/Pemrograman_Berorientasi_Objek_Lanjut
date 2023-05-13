# 3
try:
    file = open("file_tidak_ada.txt")
except FileNotFoundError:
    print("Error: File tidak ditemukan!")