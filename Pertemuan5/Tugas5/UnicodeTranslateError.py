# Mencoba mengganti karakter yang tidak dapat diterjemahkan
kalimat = "Halo, 世界!"  # Kalimat dalam bahasa Inggris dan karakter Hanzi (bahasa Tionghoa)

try:
    kalimat_terjemahan = kalimat.encode('ascii')
except UnicodeTranslateError:
    print("Error: Terdapat karakter yang tidak dapat diterjemahkan!")