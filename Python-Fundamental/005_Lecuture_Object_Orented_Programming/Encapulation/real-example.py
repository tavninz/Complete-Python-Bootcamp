
'''Consider a Student Management System where student data needs to be kept secure. You want to ensure that the student's grades can only be updated through specific methods, and you don’t want other parts of the program to directly modify the student's grade attribute.'''

class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.__grade = grade  # Private attribute to protect grades
    
    def update_grade(self, new_grade):
        if new_grade >= 0 and new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")
    
    def get_grade(self):
        return self.__grade  # Public method to get grade

# Creating a student object
student = Student("Alice", "S123", 85)

# Updating grade through a controlled method
student.update_grade(90)

# Accessing grade through a public method
print("Student Grade:", student.get_grade())

# Attempting to access the private grade directly will cause an error
# print(student.__grade)  # Uncommenting this line will raise an AttributeError
