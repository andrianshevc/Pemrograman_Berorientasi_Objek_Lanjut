my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

while True:
    try:
        item = next(my_iter)
        print(item)
    except StopIteration:
        print("Iterasi selesai.")
        break