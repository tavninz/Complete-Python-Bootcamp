'''A constructor is a special method used to initialize objects, while a destructor is used to clean up resources when the object is destroyed (in Python, it’s done automatically with __del__).'''


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        print(f"Car {self.model} of {self.year} created.")
    
    def __del__(self):
        print(f"Car {self.model} is being destroyed.")

# Creating an object
car1 = Car("Tesla", 2021)

# Deleting an object (destructor will be called)
del car1
