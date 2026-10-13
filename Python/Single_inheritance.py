class Animal:
    def eat(self):
        print("animal eats")

class Dog(Animal):
    def bark(self):
        print("dog barks")

d1=Dog()

d1.eat()
d1.bark()
