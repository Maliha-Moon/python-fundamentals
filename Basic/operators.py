""" ======================
# Python Operators 
   ======================
"""

# 1. Arithmetic Operators
# -----------------------
# Multiplication (string repetition - operator overloading)
str_multiplication = 'moon ' * 4  
print(f"String multiplication: '{str_multiplication}'")

# Exponentiation
power_result = 2 ** 5
print(f"Exponentiation (2^5): {power_result}")

# Unary minus
num = 10
print(f"Unary minus (-10): {-num}")

# True division vs Floor division
print("True division (5/2):", 5/2)  # Returns float
print("Floor division (5//2):", 5//2)  # Truncates fractional part

# 2. Comparison Operators
# ----------------------
x, y = 34, 80
print(f"Comparison (34 < 80): {x < y}")  # Returns boolean

# 3. Additional Operator Examples
# ------------------------------
# Modulus operator
print(f"Modulus (10 % 3): {10 % 3}")

# Identity operators
a = [1, 2]
b = a
print(f"Identity check (a is b): {a is b}")

# Membership operators
fruits = ['apple', 'banana']
print(f"Membership check ('apple' in fruits): {'apple' in fruits}")
