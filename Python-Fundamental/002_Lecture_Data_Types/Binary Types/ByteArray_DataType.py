''' ByteArray Data Type 
ByteArray is a mutable sequence of bytes. ByteArray is a built-in class in Python.
    - ByteArray is a mutable sequence of bytes.
    - ByteArray is a built-in class in Python.
    - ByteArray is a mutable sequence of bytes.
    - ByteArray is a built-in class in Python.
    - ByteArray is a mutable sequence of bytes.
    - ByteArray is a built-in class in Python.
    
ByteArray Methods:
- append(): It is used to add an element to the end of the ByteArray.
- extend(): It is used to add elements of an iterable to the end of the ByteArray.
- insert(): It is used to insert an element at a given index.
- pop(): It is used to remove an element from a given index.
- remove(): It is used to remove the first occurrence of an element.
- reverse(): It is used to reverse the order of elements in the ByteArray.
- clear(): It is used to remove all elements from the ByteArray.
- count(): It is used to count the number of occurrences of an element.
- index(): It is used to get the index of the first occurrence of an element.
- copy(): It is used to copy the ByteArray to another ByteArray.
- decode(): It is used to convert the ByteArray to a string.
- fromhex(): It is used to convert a hexadecimal string to a ByteArray.
- hex(): It is used to convert the ByteArray to a hexadecimal string.
- fromBase64(): It is used to convert a Base64 string to a ByteArray.
- toBase64(): It is used to convert the ByteArray to a Base64 string.
- fromBase85(): It is used to convert a Base85 string to a ByteArray.
- toBase85(): It is used to convert the ByteArray to a Base85 string.
- fromBase32(): It is used to convert a Base32 string to a ByteArray.
- toBase32(): It is used to convert the ByteArray to a Base32 string.
- fromBase16(): It is used to convert a Base16 string to a ByteArray.
- toBase16(): It is used to convert the ByteArray to a Base16 string.
- fromBase91(): It is used to convert a Base91 string to a ByteArray.
- toBase91(): It is used to convert the ByteArray to a Base91 string.
- fromBase62(): It is used to convert a Base62 string to a ByteArray.
- toBase62(): It is used to convert the ByteArray to a Base62 string.
- fromBase58(): It is used to convert a Base58 string to a ByteArray.
- toBase58(): It is used to convert the ByteArray to a Base58 string.'''

# Example 1: Create a ByteArray
# Creating a ByteArray
b = bytearray(b'Hello, Python!')
print(b)
# Output: bytearray(b'Hello, Python!')

# Example 2: Accessing Elements of ByteArray
# Creating a ByteArray
b = bytearray(b'Hello, Python!')
# Accessing elements of ByteArray
print(b[0])
print(b[1])
print(b[2])
# Output: 72
# Output: 101
# Output: 108

# Example 3: Modifying Elements of ByteArray
# Creating a ByteArray
b = bytearray(b'Hello, Python!')
# Modifying elements of ByteArray
b[0] = 65
b[1] = 66
b[2] = 67
print(b)
# Output: bytearray(b'ABClo, Python!')

# Example 4: ByteArray Methods
# Creating a ByteArray
b = bytearray(b'Hello, Python!')
# Using append() method
b.append(33)
print(b)
# Output: bytearray(b'Hello, Python!!')
# Using extend() method
b.extend(b' Welcome to Python!')
print(b)
# Output: bytearray(b'Hello, Python!! Welcome to Python!')
# Using insert() method
b.insert(13, 32)
print(b)
# Output: bytearray(b'Hello, Python! Welcome to Python!')
# Using pop() method
b.pop()
print(b)
# Output: bytearray(b'Hello, Python! Welcome to Python')
# Using remove() method
b.remove(32)
print(b)
# Output: bytearray(b'Hello, Python!Welcome to Python')
# Using revers() method
b.reverse()