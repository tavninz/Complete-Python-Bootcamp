
'''Used to modify a global variable inside a function.'''

x = 10

def modify_global():
    global x
    x = 20  # Changing global variable

modify_global()
print(x)  # Output: 20
