class Employee:
    species = "Canis familiaris" # class attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # Instance Method
    def displayInfo(self):
        return f"Name :{self.name} Age : {self.age}"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


em1 = Employee("Mosay",36)

print(em1) # return <__main__.Employee object at 0x7f2741873fa0>
print(em1.name)
print(em1.name,em1.age)

print(Employee.species) # access class attribute

print(em1.displayInfo())
print(em1.speak("Hello"))