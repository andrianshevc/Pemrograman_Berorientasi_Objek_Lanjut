try:
    # Kode yang mungkin menghasilkan SystemError
    a = 10
    b = 0
    hasil = a / b
except SystemError:
    print("Error: Terjadi kesalahan sistem!")