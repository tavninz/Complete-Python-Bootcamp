""" String format is a way to format the string in a more readable way. 

There are two ways to format the string in Python:
1. Using % operator
2. Using format() method

Way to apply the format:
1. %s - String
2. %d - Integer
3. %f - Float
4. %.<number>f - Float with number of decimal places
5. %x - Hexadecimal
6. %o - Octal
7. %e - Exponential

"""


# Usinge % operator
name = "John"
age = 25
print("Name: %s, Age: %d" % (name, age))
# Output: Name: John, Age: 25


# Using format() method
name = "John"
age = 25
print("Name: {}, Age: {}".format(name, age))
# Output: Name: John, Age: 25


# Using format() method with index
name = "John"
age = 25
print("Name: {0}, Age: {1}".format(name, age))
# Output: Name: John, Age: 25

# Using format() method with keyword
name = "John"
age = 25
print("Name: {n}, Age: {a}".format(n=name, a=age))
# Output: Name: John, Age: 25


# Using format() method with float
num = 3.1415926
print("Value of pi is: {:.2f}".format(num))
# Output: Value of pi is: 3.14

# Using format() method with hexadecimal
num = 10
print("Hexadecimal of 10 is: {:x}".format(num))
# Output: Hexadecimal of 10 is: a

# Using format() method with octal
num = 10
print("Octal of 10 is: {:o}".format(num))
# Output: Octal of 10 is: 12

# Using format() method with exponential
num = 1000000
print("Exponential of 1000000 is: {:e}".format(num))
# Output: Exponential of 1000000 is: 1.000000e+06

# Using format() method with comma separator
num = 1000000
print("Number is: {:,}".format(num))
# Output: Number is: 1,000,000

# Using format() method with comma separator and decimal places
num = 1000000
print("Number is: {:,.2f}".format(num))
# Output: Number is: 1,000,000.00

# Using format() method with comma separator and decimal places
num = 1000000
print("Number is: {:,.2f}".format(num))
# Output: Number is: 1,000,000.00

