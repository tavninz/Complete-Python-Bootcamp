from abc import ABC, abstractmethod

# Abstraction: Creating an abstract class for a Person
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_details(self):
        pass

# Inheritance: Student inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.__grade = grade  # Encapsulation: Private attribute
    
    def get_details(self):
        return f"Student Name: {self.name}, ID: {self.student_id}, Grade: {self.__grade}"

    def update_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")
    
    def get_grade(self):
        return self.__grade

# Teacher inherits from Person
class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject
    
    def get_details(self):
        return f"Teacher Name: {self.name}, ID: {self.teacher_id}, Subject: {self.subject}"

# Abstraction: Course is another class that interacts with students and teachers
class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.__students = []  # Encapsulation: Private list to store students
    
    def add_student(self, student):
        self.__students.append(student)
    
    def list_students(self):
        print(f"Students in {self.course_name}:")
        for student in self.__students:
            print(student.get_details())

# Polymorphism: Different behavior for different objects (get_details method)
def print_details(person):
    print(person.get_details())

# Creating Teacher and Student objects
teacher = Teacher("Mr. Smith", 40, "T101", "Mathematics")
student1 = Student("Alice", 18, "S123", 90)
student2 = Student("Bob", 19, "S124", 85)

# Creating a course and adding students
course = Course("Math 101", teacher)
course.add_student(student1)
course.add_student(student2)

# Using polymorphism to print details of students and teacher
print_details(student1)  # Polymorphism in action, different method for Student
print_details(teacher)   # Polymorphism in action, different method for Teacher

# Listing students in the course
course.list_students()

# Encapsulation in action: Updating student's grade via method
student1.update_grade(95)
print(f"Updated grade for Alice: {student1.get_grade()}")

# Attempting direct access to private attribute (will fail)
# print(student1.__grade)  # Uncommenting this will raise an AttributeError
