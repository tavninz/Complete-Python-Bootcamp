'''A variable declared outside a function is accessible inside functions.'''



x = 10  # Global variable

def my_function():
    print(x)  # Can access global variable

my_function()  # Output: 10
