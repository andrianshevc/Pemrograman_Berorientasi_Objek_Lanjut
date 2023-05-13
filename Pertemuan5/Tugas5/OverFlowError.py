import sys

try:
    # Melakukan operasi yang menghasilkan OverflowError
    angka_terlalu_besar = sys.maxsize + 1
except OverflowError:
    print("Error: Angka terlalu besar untuk dihandle!")