#Display name and age using parameter constructor:

class Person:
    def __init__(self, name, age):
        self.name = name     
        self.age = age       

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Sneha", 20)

person1.display()
