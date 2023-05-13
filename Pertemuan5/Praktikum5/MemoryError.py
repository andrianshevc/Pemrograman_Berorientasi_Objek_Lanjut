# 10
try:
    # Mencoba membuat string sangat panjang yang mungkin melebihi batas memori yang tersedia
    my_string = "a" * (10**10)
except MemoryError:
    print("Error: Terjadi kehabisan memori!")