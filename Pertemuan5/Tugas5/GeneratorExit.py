def my_generator():
    try:
        for i in range(1, 6):
            yield i
    except GeneratorExit:
        print("Generator dihentikan.")

# Membuat objek generator
gen = my_generator()

# Mengambil nilai dari generator
for num in gen:
    print(num)
    if num == 3:
        gen.close()  # Menghentikan generator ketika num == 3