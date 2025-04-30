"""
Dictionaries in Python
======================
A dictionary is a collection of {key:value} pairs that is:
- Ordered
- Mutable (Changeable)
- Indexed by keys
- Does not allow duplicate keys
"""

# =============================================
# Creating Dictionaries
# =============================================

# Creating a dictionary with student marks
marks = {
    "Alice": 90,
    "Bob": 88,
    "Rose": 75
}

print(marks, type(marks))  # Output the dictionary and its type

# Creating an empty dictionary
empty_dict = {}
print(type(empty_dict))  # Verify the type

# =============================================
# Accessing Dictionary Elements
# =============================================

# Accessing a value by its key
print(marks["Bob"])  # Output: 88

# =============================================
# Dictionary Methods for Accessing Data
# =============================================

# items() - returns a view of key-value pairs
print(marks.items())

# keys() - returns a view of all keys
print(marks.keys())

# values() - returns a view of all values
print(marks.values())

# =============================================
# Dictionary Methods for Modifying Data
# =============================================

# update() - updates or adds multiple key-value pairs
marks.update({"Rose": 80, "Renuka": 70})
print(marks)

# Creating another dictionary
course = {
    1: "OOP",
    2: "SPL",
    3: "OS"
}

# update() - can also merge dictionaries
marks.update(course)
print(marks)

# clear() - empties the dictionary
# course.clear()
# print(course)

# pop(key) - removes and returns the value for given key
element = marks.pop("Bob")
print(element)

# popitem() - removes and returns the last inserted item
last_item = course.popitem()
print(last_item)
