''''Stng Data Type in Python is a sequence of characters. It is a collection of characters inside single quotes, double quotes, or triple quotes.
String is immutable data type in Python. It means that once a string is created, it cannot be changed or modified.
String can be created using single quotes, double quotes, or triple quotes.
Single quotes are used to create a string containing double quotes.
Double quotes are used to create a string containing single quotes.
Triple quotes are used to create a string containing multiple lines.'''

username = "Jonh Doe"
username_1 = 'Jonh Doe'
username_2 = '''Jonh Doe'''
username_3 = """Jonh Doe"""
other_age = "25"
print(username)
print(username_1)
print(username_2)
print(username_3)
print(type(username)) # <class 'str'>
print(type(username_1)) # <class 'str'>
print(type(username_2)) # <class 'str'> 
print(type(username_3)) # <class 'str'>
print(type(other_age)) # <class 'str'>
print(username, other_age)
print(type(username), type(other_age)) # <class 'str'> <class 'str'>
print(username , int(other_age))
print(type(username), type(int(other_age))) # <class 'str'> <class 'int'>
