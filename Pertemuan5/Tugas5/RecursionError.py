def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Mencoba untuk menghitung faktorial dari angka negatif
try:
    hasil = factorial(-5)
except RecursionError:
    print("Error: Tidak dapat menghitung faktorial dari angka negatif!")