try:
    # Mendefinisikan variabel yang belum dideklarasikan
    x = y + 5
except ReferenceError:
    print("Error: Variabel tidak dideklarasikan sebelumnya!")
    