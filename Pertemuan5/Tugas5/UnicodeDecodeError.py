file_path = "file_berisi_utf8.txt"

try:
    with open(file_path, 'r', encoding='ascii') as file:
        isi_file = file.read()
except UnicodeDecodeError as e:
    print(f"Error: Terjadi kesalahan dalam decoding file: {e}")