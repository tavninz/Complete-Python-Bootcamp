
'''A variable inside a function is only accessible within that function.'''

def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  # Error! 'x' is not accessible outside the function.