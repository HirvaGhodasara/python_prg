# Lambda functions for arithmetic operations
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Division by zero"

# Input numbers and operator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Call the correct lambda based on operator
if op == '+':
    print("Result:", add(a, b))
elif op == '-':
    print("Result:", sub(a, b))
elif op == '*':
    print("Result:", mul(a, b))
elif op == '/':
    print("Result:", div(a, b))
else:
    print("Invalid operator")
