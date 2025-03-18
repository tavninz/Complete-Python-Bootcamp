'''Set Data Type is a collection of unordered and unindexed elements.
It is written with curly brackets {}.
It is mutable and does not allow duplicate elements.
It is used to perform mathematical set operations like union, intersection, difference, and symmetric difference.

Set Data Type is used to store multiple items in a single variable.
It is a collection of unique elements.
It is mutable, which means it can be changed after creation.
It is unordered, which means that the elements are not ordered.
It is unindexed, which means that the elements do not have a specific index.

Set Methods:
add() - Adds an element to the set
clear() - Removes all the elements from the set
copy() - Returns a copy of the set
difference() - Returns a set containing the difference between two or more sets
difference_update() - Removes the items in this set that are also included in another, specified set
discard() - Remove the specified item
intersection() - Returns a set, that is the intersection of two other sets
intersection_update() - Removes the items in this set that are not present in other, specified set(s)
isdisjoint() - Returns whether two sets have a intersection or not
issubset() - Returns whether another set contains this set or not
issuperset() - Returns whether this set contains another set or not
pop() - Removes an element from the set
remove() - Removes the specified element
symmetric_difference() - Returns a set with the symmetric differences of two sets
symmetric_difference_update() - inserts the symmetric differences from this set and another
union() - Return a set containing the union of sets
update() - Update the set with the union of this set and others
'''

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1)
print(set2)
print("===============")
print(set1.union(set2)) # union() method returns a set that contains all items from the original set, and all items from the specified sets.
print(set1.difference(set2)) # difference() method returns a set that contains the difference between two sets.
# Output: {1, 2, 3}
print("===============")
print(set1.intersection(set2)) # intersection() method returns a set that contains the similarity between two or more sets.
# Output: {4, 5}
print("===============")
print(set1.symmetric_difference(set2)) # symmetric_difference() method returns a set that contains all items from both set, except items that are present in both sets.
# Output: {1, 2, 3, 6, 7, 8}
print("===============")
print(set1.update(set2)) # update() method inserts the items in set2 into set1.
print(set1)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("===============")
print(set2)
# Output: {4, 5, 6, 7, 8}
print("===============")
print(set1.issubset(set2)) # issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
# Output: False
print("===============")
print(set1.issuperset(set2)) # issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
# Output: True
print("===============")
print(set1.isdisjoint(set2)) # isdisjoint() method returns True if none of the items are present in both sets, otherwise it retuns False.
# Output: False
print("===============")
print(set1.pop()) # pop() method removes a random item from the set.
print(set1)
# Output: {2, 3, 4, 5, 6, 7, 8}
print("===============")
print(set1.remove(2)) # remove() method removes the specified element from the set.
print(set1)
# Output: {3, 4, 5, 6, 7, 8}
print("===============")
print(set1.discard(3)) # discard() method removes the specified item from the set.
print(set1)
# Output: {4, 5, 6, 7, 8}
print("===============")
print(set1.clear()) # clear() method removes all the elements from the set.
print(set1)
# Output: set()
print("===============")
print(set1.copy()) # copy() method returns a copy of the set.
# Output: {4, 5, 6, 7, 8}
print("===============")
print(set1) # set1 is empty now.    Output: set()
print(set2)
print(set2.copy()) # copy() method returns a copy of the set.
print(set2) # set2 is not empty.    Output: {4, 5, 6, 7, 8}
print(set2.clear()) # clear() method removes all the elements from the set.
print(set2) # set2 is empty now.    Output: set()
print(set1)
print(set2)
# print(set1[0]) # TypeError: 'set' object is not subscriptable
# print(set2[0]) # TypeError: 'set' object is not subscriptable
# print(set1[1]) # TypeError: 'set' object is not subscriptable
# print(set2[1]) # TypeError: 'set' object is not subscriptable
# print(set1[2]) # TypeError: 'set' object is not subscriptable
# print(set2[2]) # TypeError: 'set' object is not subscriptable
# print(set1[3]) # TypeError: 'set' object is not subscriptable
# print(set2[3]) # TypeError: 'set' object is not subscriptable
# print(set1[4]) # TypeError: 'set' object is not subscriptable
# print(set2[4]) # TypeError: 'set' object is not subscriptable
# print(set1[5]) # TypeError: 'set' object is not subscriptable
# print(set2[5]) # TypeError: 'set' object is not subscriptable
# print(set1[6]) # TypeError: 'set' object is not subscriptable
# print(set2[6]) # TypeError: 'set' object is not subscriptable
# print(set1[7]) # TypeError: 'set' object is not subscriptable