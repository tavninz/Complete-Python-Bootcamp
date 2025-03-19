'''1. What is a Function?
A function in Python is a block of reusable code that performs a specific task. Functions help in organizing and structuring code efficiently. They allow code reuse, making programs modular and easier to debug.

2. Why Use Functions?
Code Reusability: Write once, use multiple times.
Modularity: Break complex programs into smaller, manageable parts.
Readability: Makes code cleaner and more understandable.
Easy Debugging: Debugging functions is simpler than debugging large scripts.'''

# simple function
def sayHello():
    print("Hello World")

# function arguments
def SpkeakName(name):
    print(f"Hello {name}".format(name))

# other function arguments
def calScore(subj1,subj2):
    '''this function accept two argument: subject-1 and subject-2'''
    result = subj1 + subj2
    print("Sum : ",result)

# return function
def checkYear(age):
    return 2024 - age

# Default Argument Values
def SayName(name="Stev Job"):
    return f"Hello {name}".format(name)


# Keyword Arguments
def getInfo(name,age=27,state='Phnom Penh', roll='Admin', position='IT-Infra'):
    print(f"My name is {name}.".format(name))
    print(f"I'm {age} year old.".format(age))
    print(f"I work as {roll} in company.".format(roll))
    print(f"My Major is {position}.".format(position))


# *args
    '''The *args is accept many of arguments. and return as list'''
def Myfavor(name, *favor):
    items = ""
    for item in favor:
        items += item + ","
        # print(item)
    print(f"My name is {name}, My Favor's {items}".format(name,items))

# **kwargs
    '''The **kwargs is accept many of keyword arguments. and return as dictionary'''
def studentList(**student):
    for key,value in student.items():
        print("{} : {}".format(key,value))


''''===================== II =========================='''
# call all above function
sayHello()
SpkeakName("Jupiter")
calScore(100,69)
myAge = checkYear(28)
print(myAge)

print(SayName())
print(SayName("Jes Basovs"))
print('\n')

getInfo("Joseth")                             # 1 positional argument
getInfo(name="Joseth")                        # 1 keyword argument
getInfo("Sopha",35)                           # 2 keyword arguments
getInfo(state="Prey Veng", name='Bruno')      # 2 keyword arguments
print('\n')
getInfo('Battambang','Users','Administrator') # 3 positional arguments
getInfo('Jonh', state='Koh Kong')             # 1 positional, 1 keyword


# example *args
Myfavor("Haley","BMW","HONDA","FORD")

# example **kwargs

studentList(firstName="Bruno",lastName="Mark",age=36,state="Phnom Penh",field="Information Security")