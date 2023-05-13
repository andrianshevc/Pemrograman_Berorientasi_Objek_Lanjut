teks = "Halo, 世界!"  # Mengandung karakter unicode yang tidak dapat diencode menjadi ASCII

try:
    teks_ascii = teks.encode('ascii')  # Mengencode teks menjadi ASCII
except UnicodeEncodeError as e:
    print(f"Error: {e}")