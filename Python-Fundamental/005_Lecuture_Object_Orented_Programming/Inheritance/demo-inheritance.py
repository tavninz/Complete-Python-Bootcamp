'''Inheritance allows one class to inherit the properties and methods of another class, enabling code reuse and extension. A child class can override methods of a parent class.'''

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Another child class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Creating objects of child classes
dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()  # Rex barks.
cat.speak()  # Whiskers meows.
