#  4

dict_data = {"nama": "John", "umur": 30, "pekerjaan": "developer"}

try:
    # Mengakses key yang tidak ada dalam dictionary
    print(dict_data["alamat"])
except KeyError:
    print("Error: Key tidak ditemukan dalam dictionary!")