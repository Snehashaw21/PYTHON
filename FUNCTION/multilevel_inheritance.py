#Multilevel Inheritance:

class Animal:
    def eat(self):
        print("Animal eats food")

class Bird(Animal):
    def fly(self):
        print("Bird is flying")

class Parrot(Bird):
    def talk(self):
        print("Parrot is talking")

p = Parrot()
p.eat()
p.fly()
p.talk()
