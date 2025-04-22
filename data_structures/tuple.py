"""
Tuple Operations in Python
Demonstrating properties and methods of tuples
"""

# Tuple Basics
empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>

# Single-element tuple (requires trailing comma)
single_element = (1,)
print(type(single_element))

# Multi-element tuple with mixed types
fruits = (100, 200, "Mango", 100, "Lichi", 30.75)
print(type(fruits))
print(fruits)

# Tuples are immutable (unlike lists)
# fruits[0] = 50  # This would raise TypeError

# Tuple Methods
# count() - returns number of occurrences
print(fruits.count(100))  # Output: 2

# index() - returns first index of value
print(fruits.index("Lichi"))  # Output: 4

# Tuple Unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x, y, z)  # Output: 1 2 3

# sum() - works with numeric tuples
numbers = (10, 20, 30)
print(sum(numbers))  # Output: 60
