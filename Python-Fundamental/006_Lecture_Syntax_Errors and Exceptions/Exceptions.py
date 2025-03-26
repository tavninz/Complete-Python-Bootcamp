""" Exceptions is an error that occurs during the execution of a program. 

Type of Exceptions:
1. AssertionError
2. AttributeError
3. EOFError
4. FloatingPointError
5. GeneratorExit
6. ImportError
7. IndexError
8. KeyError
9. KeyboardInterrupt
10. MemoryError
11. NameError
12. NotImplementedError"""



# Example 1: AssertionError
# assert False, "AssertionError: The condition is False"
# Output: AssertionError: The condition is False

# Handle Error
# try:
#     assert False, "AssertionError: The condition is False"
# except AssertionError as e:
#     print(e)

# Output: AssertionError: The condition is False

# Example 2: AttributeError
# x = 10
# print(x.upper())
# AttributeError: 'int' object has no attribute 'upper'

# Handle Error
# try:
#     x = 10
#     print(x.upper())
# except AttributeError as e:
#     print(e)
# AttributeError: 'int' object has no attribute 'upper'
# Output: 'int' object has no attribute 'upper'


# Example 3: EOFError
# x = input("Input number of age: ")
# EOFError: EOF when reading a line

# Handle Error
# try:
#     x = input("Input number of age: ")
# except EOFError as e:
#     print(e)
# Output: EOF when reading a line


# Example 4: FloatingPointError
# print(1 / 0)
# ZeroDivisionError: division by zero

# Handle Error
# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print(e)
# Output: division by zero


# Example 5: GeneratorExit
# def generator():
#     try:
#         yield 1

#     except GeneratorExit:
#         print("GeneratorExit: Closing the generator")

# g = generator()
# next(g)
# g.close()
# GeneratorExit: Closing the generator
# Handle Error
# def generator():
#     try:
#         yield 1

# Output: 1
#     except GeneratorExit:
#         print("GeneratorExit: Closing the generator")


# Example 6: ImportError
# import xyz
# ModuleNotFoundError: No module named 'xyz'

# Handle Error
# try:
#     import xyz
#     except ModuleNotFoundError as e:
#            print(e)


# Example 7: IndexError
# x = [1, 2, 3]
# print(x[4])
# IndexError

# Handle Error
# try:
#     x = [1, 2, 3]
#     print(x[4])
# except IndexError as e:
#     print(e)
# IndexError: list index out of range
# Output: list index out of range


# Example 8: KeyError
# x = {1: 'a', 2: 'b', 3: 'c'}
# print(x[4])
# KeyError: 4

# Example 9: KeyboardInterrupt
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("KeyboardInterrupt: You have interrupted the program")
# KeyboardInterrupt: You have interrupted the program

# Example 10: MemoryError
# x = []
# while True:
#     x.append(1)
# MemoryError

# Example 11: NameError
# print(x)
# NameError: name 'x' is not defined

# Example 12: NotImplementedError
# class A:
#     def show(self):
#         raise NotImplementedError("NotImplementedError: You have to provide the implementation")



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
