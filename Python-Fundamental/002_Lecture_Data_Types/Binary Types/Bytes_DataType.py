''' Bytes Data Type
Bytes data type is used to store a sequence of bytes.
It is an immutable data type.
It is an array of bytes.

Bytes Methods:
capitalize() - Converts the first character to upper case
center() - Returns a centered string
count() - Returns the number of times a specified value occurs in a string
decode() - Decodes the byte object
endswith() - Returns true if the string ends with the specified value
expandtabs() - Sets the tab size of the string
find() - Searches the string for a specified value and returns the position of where it was found
fromhex() - Returns a bytes object from a hex string
hex() - Converts a number into a hexadecimal value
index() - Searches the string for a specified value and returns the position of where it was found
isalnum() - Returns True if all characters in the string are alphanumeric
isalpha() - Returns True if all characters in the string are in the alphabet
isascii() - Returns True if all characters in the string are ascii characters
isdecimal() - Returns True if all characters in the string are decimals
isdigit() - Returns True if all characters in the string are digits
isidentifier() - Returns True if the string is an identifier
islower() - Returns True if all characters in the string are lower case
isnumeric() - Returns True if all characters in the string are numeric
isprintable() - Returns True if all characters in the string are printable
isspace() - Returns True if all characters in the string are whitespaces
istitle() - Returns True if the string follows the rules of a title
isupper() - Returns True if all characters in the string are upper case
join() - Joins the elements of an iterable to the end of the string
ljust() - Returns a left justified version of the string
lower() - Converts a string into lower case
lstrip() - Returns a left trim version of the string
maketrans() - Returns a translation table to be used in translations
partition() - Returns a tuple where the string is parted into three parts
replace() - Returns a string where a specified value is replaced with a specified value
rfind() - Searches the string for a specified value and returns the last position of where it was found
rindex() - Searches the string for a specified value and returns the last position of where it was found
rjust() - Returns a right justified version of the string
rpartition() - Returns a tuple where the string is parted into three parts
rsplit() - Splits the string at the specified separator, and returns a list
rstrip() - Returns a right trim version of the string
split() - Splits the string at the specified separator, and returns a list
splitlines() - Splits the string at line breaks and returns a list
startswith() - Returns true if the string starts with the specified value
strip() - Returns a trimmed version of the string
swapcase() - Swaps cases, lower case becomes upper case and vice versa
title() - Converts the first character of each word to upper case
translate() - Returns a translated string
upper() - Converts a string into upper case
zfill() - Fills the string with a specified number of 0 values at the beginning
'''
# Example:
bytes1 = b"Hello, World!"
print(bytes1)
# Output: b'Hello, World!'
# Example:
bytes2 = bytes(10)
print(bytes2)
# Output: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# Example:
bytes3 = bytes([1,2,3,4,5])
print(bytes3)
# Output: b'\x01\x02\x03\x04\x05'
# Example:
bytes4 = bytes("Hello, World!", "utf-8")
print(bytes4)
# Output: b'Hello, World!'
# Example:
bytes5 = bytes("Hello, World!", "ascii")
print(bytes5)
# Output: b'Hello, World!'
# Example:
bytes6 = bytes("Hello, World!", "utf-16")
print(bytes6)
# Output: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00!\x00'
# Example:
bytes7 = bytes("Hello, World!", "utf-32")
print(bytes7)
# Output: b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00,\x00\x00\x00 \x00\x00\x00W\x00\x00\x00o\x00\x00\x00r\x00\x00\x00l\x00\x00\x00d\x00\x00\x00!\x00\x00\x00'
# Example:
bytes8 = bytes("Hello, World!", "utf-64")
print(bytes8)
# Output: b'\xff\xfe\x00\x00\x00\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00W\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00r\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00'

# capitalize() method
# The capitalize() method converts the first character to upper case.
# Syntax:
# bytes.capitalize()
# Parameters:
# The capitalize() method doesn't take any parameters.
# Return Value:
# The capitalize() method returns a string where the first character is upper case.
# Note: The capitalize() method doesn't change the original string.
# Example:
bytes9 = bytes("Hello, World!", "utf-8")
print(bytes9.capitalize()) # capitalize() method converts the first character to upper case.

# center() method
# The center() method returns a centered string.
# Syntax:
# bytes.center(length, character)
# Parameters:
# length - The length of the returned string.
# character (optional) - The character to fill the missing space on the left and right side.
# Return Value:
# The center() method returns a string where the original string is centered.
# Example:
bytes10 = bytes("Hello, World!", "utf-8")
print(bytes10.center(20)) # center() method returns a centered string.
# Output: b'  Hello, World!   '
# Example:
bytes11 = bytes("Hello, World!", "utf-8")
print(bytes11.center(20, "*")) # center() method returns a centered string.
# Output: b'**Hello, World!***'
# Example:
bytes12 = bytes("Hello, World!", "utf-8")
print(bytes12.center(30, "*")) # center() method returns a centered string.
# Output: b'*****Hello, World!******'   # 5 * on left side, 6 * on right side.
# Example:
bytes13 = bytes("Hello, World!", "utf-8")
print(bytes13.center(30, " ")) # center() method returns a centered string.
# Output: b'     Hello, World!      '   # 5 spaces on left side, 6 spaces on right side.    # 11 spaces in total.

# count() method
# The count() method returns the number of times a specified value occurs in a string.
# Syntax:
# bytes.count(value, start, end)
# Parameters:
# value - The value to search for.
# start (optional) - The start position to start the search.
# end (optional) - The end position to end the search.
# Return Value:
# The count() method returns the number of times the specified value appears in the string.
# Example:
bytes14 = bytes("Hello, World!", "utf-8")
print(bytes14.count("o")) # count() method returns the number of times the specified value appears in the string.
# Output: 2
# Example:
bytes15 = bytes("Hello, World!", "utf-8")
print(bytes15.count("l")) # count() method returns the number of times the specified value appears in the string.
# Output: 3
# Example:
bytes16 = bytes("Hello, World!", "utf-8")
print(bytes16.count("l", 0, 5)) # count() method returns the number of times the specified value appears in the string.
# Output: 2
# Example:
bytes17 = bytes("Hello, World!", "utf-8")
print(bytes17.count("l", 0, 10)) # count() method returns the number of times the specified value appears in the string.
# Output: 3
# Example:
bytes18 = bytes("Hello, World!", "utf-8")
print(bytes18.count("l", 0, 15)) # count() method returns the number of times the specified value appears in the string.
# Output: 3
# Example:
bytes19 = bytes("Hello, World!", "utf-8")
print(bytes19.count("l", 0, 20)) # count() method returns the number of times the specified value appears in the string.    # 20 is greater than the length of the string.
# Output: 3
# Example:
bytes20 = bytes("Hello, World!", "utf-8")
print(bytes20.count("l", 0, 25)) # count() method returns the number of times the specified value appears in the string.    # 25 is greater than the length of the string.
# Output: 3
# Example:
bytes21 = bytes("Hello, World!", "utf-8")
print(bytes21.count("l", 0, 30)) # count() method returns the number of times the specified value appears in the string.    # 30 is greater than the length of the string.
# Output: 3
# Example:
bytes22 = bytes("Hello, World!", "utf-8")
print(bytes22.count("l", 0, 0)) # count() method returns the number of times the specified value appears in the string.    # 0 is less than the length of the string.
# Output: 0
# Example:
bytes23 = bytes("Hello, World!", "utf-8")
print(bytes23.count("l", 0, -1)) # count() method returns the number of times the specified value appears in the string.    # -1 is less than the length of the string.
# Output: 3
# Example:
bytes24 = bytes("Hello, World!", "utf-8")
print(bytes24.count("l", 0, -5)) # count() method returns the number of times the specified value appears in the string.    # -5 is less than the length of the string.
# Output: 2
# Example:
bytes25 = bytes("Hello, World!", "utf-8")
print(bytes25.count("l", 0, -10)) # count() method returns the number of times the specified value appears in the string.    # -10 is less than the length of the string.
# Output: 1
# Example:
bytes26 = bytes("Hello, World!", "utf-8")
print(bytes26.count("l", 0, -15)) # count() method returns the number of times the specified value appears in the string.    # -15 is less than the length of the string.
# Output: 0
# Example:
bytes27 = bytes("Hello, World!", "utf-8")
print(bytes27.count("l", 0, -20)) # count() method returns the number of times the specified value appears in the string.    # -20 is less than the length of the string.
