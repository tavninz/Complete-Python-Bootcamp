"""Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:"""


# 10 * (1/0)

# ZeroDivisionError: division by zero

# 10 * (root/2)
# NameError: name 'root' is not defined


# Handle Error

while True:
    try:
        x = input("Input number of age: ")
        x = 2024 - x # TypeError: unsupported operand type(s) for -: 'int' and 'str'
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    
    except TypeError:
        print("Oops!  That was no unsupported types.  Try again...")
        break
