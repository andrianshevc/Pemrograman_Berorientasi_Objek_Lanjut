class Animal:
    def speak(self):
        raise NotImplementedError("Metode 'speak' belum diimplementasikan!")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    pass

my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())  # Output: Woof!
print(my_cat.speak())  # Raises NotImplementedError: Metode 'speak' belum diimplementasikan!