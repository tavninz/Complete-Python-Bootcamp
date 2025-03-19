''' None Type in Python 

In Python, NoneType represents the type of the None object. None is a special constant that signifies the absence of a value or a null value. 

Key point:

Singleton Object: None is the only instance of NoneType, meaning there's only one None in Python.

Used as a Default Return Value: Functions that do not explicitly return anything return None by default.

Falsy in Boolean Context: None evaluates to False in boolean expressions.
Commonly Used for Initialization: Variables can be initialized with None before being assigned actual values.'''


x = None
print(x)
print(type(x))  # Output: <class 'NoneType'>



def my_function():
    pass

result = my_function()
print(result)  # Output: None
print(type(result))  # Output: <class 'NoneType'>



x = None
if x is None:
    print("x is None")
    
    
x = None
if not x:  # Equivalent to if x is None or x is False
    print("x is falsy")