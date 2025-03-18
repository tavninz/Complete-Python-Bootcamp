''' Frosent Set Data Type in Python
Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.
Frozensets can be created using the function frozenset().

Rules for Frozen Set:
The elements in a frozen set remain the same after creation.
Frozen sets can be used as keys in Dictionary or as elements of another set.
The syntax of frozenset() is:
frozenset([iterable])

Frozen Set Methods:
copy() - Returns a copy of the set
difference() - Returns a set containing the difference between two or more sets
intersection() - Returns a set, that is the intersection of two other sets
isdisjoint() - Returns whether two sets have a intersection or not
issubset() - Returns whether another set contains this set or not
issuperset() - Returns whether this set contains another set or not
symmetric_difference() - Returns a set with the symmetric differences of two sets
union() - Return a set containing the union of sets
'''

frozenset1 = frozenset([1,2,3,4,5])
frozenset2 = frozenset([4,5,6,7,8])
print(frozenset1)
print(frozenset2)
print("===============")
print(frozenset1.union(frozenset2)) # union() method returns a set that contains all items from the original set, and all items from the specified sets.
# Output: frozenset({1, 2, 3, 4, 5, 6, 7, 8})
print("===============")
print(frozenset1.difference(frozenset2)) # difference() method returns a set that contains the difference between two sets.
# Output: frozenset({1, 2, 3})
print("===============")
print(frozenset1.intersection(frozenset2)) # intersection() method returns a set that contains the similarity between two or more sets.
# Output: frozenset({4, 5})
print("===============")
print(frozenset1.symmetric_difference(frozenset2)) # symmetric_difference() method returns a set that contains all items from both set, except items that are present in both sets.
# Output: frozenset({1, 2, 3, 6, 7, 8})
print("===============")
print(frozenset1.issubset(frozenset2)) # issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
# Output: False
print("===============")
print(frozenset1.issuperset(frozenset2)) # issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
# Output: False
print("===============")
print(frozenset1.isdisjoint(frozenset2)) # isdisjoint() method returns True if none of the items are present in both sets, otherwise it retuns False.
# Output: False
print("===============")
print(frozenset1.copy()) # copy() method returns a copy of the set.
# Output: frozenset({1, 2, 3, 4, 5})