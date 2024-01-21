'''
PYTHON 2 : print "print this info"  -> statement
PYTHON 3 : print("print this info") -> function

Option for PYTHON 2:
from __future__ import print_function
'''

# use single or double quotes

str = "Hello World"
str2 = 'Hello Python'

print(str[0]) # print the first letter
print(str[2:]) # print from the third letter onwards
print(str[:3]) # print up to the third letter
print(str[-1]) # print the last letter
print(str[:-1]) # print up to the last letter
print(str[::1]) # print each letter, step sizes of one
print(str[::2]) # print every second letter
print(str[::-1])  # print the string in reverse

# strings are immutable:  str[2] = 'e' will produce an error

str = str + "Baloon"
print(str)

str * 5
print(str)

print(len(str))
print(str.capitalize()) # capitalize
print(str.upper()) # upper case
print(str.lower()) # lower case
print(str.split())  # split string by blank space (default)
print(str.split('w')) # split string by element

# format string
name = "Peter"
age = 45
print(f"Welcome to {name} you are {age} year old.")
print("Hello {} and your age is {}".format(name,age))

print()