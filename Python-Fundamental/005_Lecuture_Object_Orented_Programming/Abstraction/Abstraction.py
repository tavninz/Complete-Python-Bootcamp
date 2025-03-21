'''Abstraction hides implementation details and only exposes essential features.'''

'''Abstraction hides the complexity of the system by exposing only necessary details. In Python, this is typically done using abstract classes (via the abc module) or just defining clear interfaces for the class.'''


from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car moves on wheels"

class Boat(Vehicle):
    def move(self):
        return "Boat moves on water"

car = Car()
boat = Boat()

print(car.move())  # Output: Car moves on wheels
print(boat.move())  # Output: Boat moves on water
