text = b'\xc3\x28'  # Menyimpan sequence byte yang salah

try:
    decoded_text = text.decode('utf-8')  # Mendekodekan sequence byte menjadi string UTF-8
except UnicodeError:
    print("Error: Terjadi kesalahan dalam dekodekan teks!")