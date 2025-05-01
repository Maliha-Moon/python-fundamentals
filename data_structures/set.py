"""
Sets in Python:
- Unordered collection
- Unindexed
- No duplicates
- Unchangeable (but can add/remove elements)
"""

# ====================
# SET CREATION
# ====================

# Empty set (don't use {} as it creates a dictionary)
empty_set = set()
print(f"Type of empty_set: {type(empty_set)}")

# Set creation (duplicates automatically removed)
numbers = {1, 2, 3, 3, 3, 4, 5}
print(f"\nNumbers set: {numbers}")

mixed_set = {"Carle", 19, False, 5.5, 19}
print(f"Mixed set: {mixed_set}")

# ====================
# BASIC SET OPERATIONS
# ====================

# add() - Add single element
numbers.add(566)
print(f"\nAfter adding 566: {numbers}")

# update() - Add multiple elements from iterable
numbers.update(["orange", 100.75])
print(f"After adding multiple elements: {numbers}")

# update() - Merge two sets
numbers.update(mixed_set)
print(f"After merging with mixed_set: {numbers}")

# len() - Get set length
print(f"\nLength of numbers set: {len(numbers)}")

# in - Check membership
print("\nMembership check:")
if "Carle" in mixed_set:
    print("Carle is present")
else:
    print("Carle is not present")

# remove() - Remove element (raises KeyError if not found)
numbers.remove(4)
print(f"\nAfter removing 4: {numbers}")

# discard() - Remove element (no error if not found)
numbers.discard(1)
print(f"After discarding 1: {numbers}")
numbers.discard(10)  # No error
print(f"After discarding 10 (not present): {numbers}")

# ====================
# MATHEMATICAL OPERATIONS
# ====================

set1 = {1, 78, 120, 99}
set2 = {22, 67, 1, 150, 78}

# union() (|) - Combine sets
print("\nSet Operations:")
print(f"Union: {set1.union(set2)}")
print(f"Union using |: {set1 | set2}")

# intersection() (&) - Common elements
print(f"\nIntersection: {set1.intersection(set2)}")
print(f"Intersection using &: {set1 & set2}")

# symmetric_difference() (^) - Elements in either but not both
print(f"\nSymmetric difference: {set1.symmetric_difference(set2)}")

# difference() (-) - Elements in set1 but not set2
print(f"\nDifference (set1 - set2): {set1.difference(set2)}")

# ====================
# SET COMPARISONS
# ====================

s1 = {1, 78}
s2 = {22, 67, 1, 150, 78}

#isdisjoint() – Check if sets have no common elements
print(s1.isdisjoint(s2))

# issuperset() - check if all elemets of another set is present
print(s2.issuperset(s1)) # check if elements of set1 is present in set2 or not

# issubset() - check if all elements are present in another set
print(s1.issubset(s2))

# ====================
# CAUTIONS & EDGE CASES
# ====================

# Integer and float equality in sets
unique_set = {20, 20.0}
print(f"\nLength of {20, 20.0}: {len(unique_set)}")  # Output: 1 (20 == 20.0)

# Sets cannot contain mutable elements like lists
try:
    invalid_set = {"Carle", 19, False, 5.5, 19, [1, 2]}
except TypeError as e:
    print(f"\nError when creating set with list: {e}")
