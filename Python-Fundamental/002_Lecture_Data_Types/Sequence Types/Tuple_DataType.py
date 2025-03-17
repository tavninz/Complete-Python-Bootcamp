''' Tuple Data Type is a collection of items. It is ordered and immutable. it means that items in a tuple are stored in a sequence and cannot be modified. Tuple is defined by using parentheses () and items are separated by commas. Tuple can have items of different data types. Tuple can have duplicate items. Tuple can have nested tuples. Tuple can be empty. Tuple is iterable. Tuple is immutable.
    Tuple is defined by using parentheses () and items are separated by commas.
    Tuple can have items of different data types.
    Tuple can have duplicate items.
    Tuple can have nested tuples.
    Tuple can be empty.
    Tuple is iterable.
    Tuple is immutable.'''
    
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

# Tuple can have items of different data types.
tuple2 = (1, 2.5, 'Hello', True)
print(tuple2)
# Tuple can have duplicate items.
tuple3 = (1, 2, 3, 4, 4, 5)
print(tuple3)
# Tuple can have nested tuples.
tuple4 = (1, 2, (3, 4), 5)
print(tuple4)
# Tuple can be empty.
tuple5 = ()
print(tuple5)
# Tuple is iterable.
for i in tuple1:
    print(i)
# Tuple is immutable.
# tuple1[0] = 10
# print(tuple1)
# TypeError: 'tuple' object does not support item assignment
# Tuple can have items of different data types.
# tuple1[1] = 'Hello'
# print(tuple1)
# TypeError: 'tuple' object does not support item assignment
# Tuple can have duplicate items.
# tuple1[2] = 10
# print(tuple1)
# TypeError: 'tuple' object does not support item assignment
# Tuple can have nested tuples.
# tuple1[3] = (1, 2)
# print(tuple1)
# TypeError: 'tuple' object does not support item assignment
# Tuple can be empty.
# tuple1[4] = ()
# print(tuple1)
# TypeError: 'tuple' object does not support item assignment
# Tuple is iterable.
for i in tuple1:
    print(i)
# Tuple is immutable.
# tuple1[0] = 10
# print(tuple1)