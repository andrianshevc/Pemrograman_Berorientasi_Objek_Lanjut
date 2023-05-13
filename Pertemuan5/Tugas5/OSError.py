import os

try:
    # Kode untuk operasi pada file atau direktori
    # yang dapat menghasilkan OSError
    file_path = "file_tidak_ada.txt"
    with open(file_path, "r") as file:
        # Melakukan operasi pada file yang ada
        print(file.read())
except OSError as e:
    print(f"Error: {e}")