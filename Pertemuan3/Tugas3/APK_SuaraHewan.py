import pygame

# list nama untuk hewan dan path file suara
hewan = [
    {"nama": "ayam", "path": "suara-hewan/Ayam.mp3"},
    {"nama": "bebek", "path": "suara-hewan/bebek.mp3"},
    {"nama": "kambing", "path": "suara-hewan/Kambing.mp3"},
    {"nama": "kucing", "path": "suara-hewan/Kucing.mp3"},
    {"nama": "sapi", "path": "suara-hewan/Sapi.mp3"},
    {"nama": "anjing", "path": "suara-hewan/Anjing.mp3"},
    {"nama": "kodok", "path": "suara-hewan\Kodok.mp3"},
    {"nama": "burung elang", "path": "suara-hewan/burung elang.mp3"},
    {"nama": "nyamuk", "path": "suara-hewan/Nyamuk.mp3"},
    {"nama": "babi", "path": "suara-hewan/Babi.mp3"},
]

# inisialisasi library pygame
pygame.init()

# loop untuk menampilkan daftar hewan dan memainkan suara hewan yang dipilih
while True:
    print("Pilih hewan yang ingin didengarkan suaranya:")
    for i, item in enumerate(hewan):
        print(f"{i+1}. {item['nama']}")

    pilihan = int(input("Masukkan nomor hewan: "))
    if 1 <= pilihan <= len(hewan):
        # mainkan file suara untuk hewan yang dipilih
        suara_hewan = pygame.mixer.Sound(hewan[pilihan-1]["path"])
        suara_hewan.play()
        pygame.time.wait(1000)  # tunggu 1 detik sebelum mengakhiri program
    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")