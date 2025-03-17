''' List Data Type in Python is a collection of items. It is ordered and mutable. it means that items in a list are stored in a sequence and can be modified. List is defined by using square brackets [] and items are separated by commas. List can have items of different data types. List can have duplicate items. List can have nested lists. List can be empty. List is iterable. List is mutable.
    List is defined by using square brackets [] and items are separated by commas.
    List can have items of different data types.
    List can have duplicate items.
    List can have nested lists.
    List can be empty.
    List is iterable.
    List is mutable.'''
    
list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))

# List can have items of different data types.
list2 = [1, 2.5, 'Hello', True]
print(list2)
# List can have duplicate items.
list3 = [1, 2, 3, 4, 4, 5]
print(list3)
# List can have nested lists.
list4 = [1, 2, [3, 4], 5]
print(list4)
# List can be empty.
list5 = []
print(list5)
# List is iterable.
for i in list1:
    print(i)
# List is mutable. 
list1[0] = 10
print(list1)
# List can have items of different data types.
list1[1] = 'Hello'
print(list1)
# List can have duplicate items.
list1[2] = 10
print(list1)
# List can have nested lists.
list1[3] = [1, 2]
print(list1)
# List can be empty.
list1[4] = []
print(list1)
# List is iterable.
for i in list1:
    print(i)