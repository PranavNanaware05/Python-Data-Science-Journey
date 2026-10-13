class Animal:
 def eat(self):
  print("Animal Eat")

class Dog(Animal):
 def bark(self):
  print("Dog Barks")


class Puppy(Dog):
 def play(self):
  print("Puppy Playing")


p1=Puppy()

p1.eat()
p1.bark()
p1.play()
   