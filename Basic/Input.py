# Demonstrating Python input() and type conversion
num1 = input("Enter number 1: ")  # Input returns string by default
num2 = input("Enter number 2: ")

# Show original input types (always str)
print(f"Type of num1: {type(num1)}, Type of num2: {type(num2)}")  

# Convert to int and perform arithmetic
sum_result = int(num1) + int(num2)
print(f"Sum: {sum_result}")

# Calculate square of second number
square_result = int(num2) ** 2  
print(f"Square of num2: {square_result}")
