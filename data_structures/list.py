"""
List Operations and Methods
"""

# List can store values of any data type
fruits = ["Apple", "Orange", "Banana", 100, False, "Mango", 50.75]
print(fruits)
print(fruits[0])

# Lists are mutable (unlike strings)
fruits[0] = "Grape"  
print(fruits[0])


"""
List Methods
"""

# Slicing
print(fruits[-6:])

# append(element) - adds element to the end
fruits.append("Lichi")
print(fruits)

# extend(list) - adds another list to the end
fruits.extend([200, 300, "Dragon"])
print(fruits)

# sort() - sorts the list (works with homogeneous numeric lists)
numbers = [1, 90, 12, 34, 12, 45]
numbers.sort()
print(numbers)

# reverse() - reverses the list in place
numbers.reverse()
print(numbers)

# insert(index, element) - inserts element at specified position
numbers.insert(0, 25) 
print(numbers)

# pop(index) - removes and returns element at index
val = numbers.pop(3)
print(val)
print(numbers)

# remove(element) - removes first occurrence of element
numbers.remove(12)
print(numbers)
