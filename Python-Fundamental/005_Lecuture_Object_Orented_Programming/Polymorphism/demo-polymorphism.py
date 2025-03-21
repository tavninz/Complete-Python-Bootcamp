'''Polymorphism means having many forms. In Python, it is often achieved through method overriding and dynamic method resolution. It allows us to call the same method name on different objects, but the actual method that gets called depends on the type of the object.'''


class Bird:
    def speak(self):
        print("Tweet!")

class Dog:
    def speak(self):
        print("Woof!")

# Demonstrating polymorphism
def animal_sound(animal):
    animal.speak()  # Will call the appropriate method based on the object's class

bird = Bird()
dog = Dog()

animal_sound(bird)  # Tweet!
animal_sound(dog)   # Woof!
