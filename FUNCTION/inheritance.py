#Single Inheritance:

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()   
d.bark()  
