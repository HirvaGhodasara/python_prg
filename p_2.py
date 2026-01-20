# Program to perform arithmetic operation based on operator input

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter arithmetic operator (+, -, *, /): ")

if op == '+':
    result = a + b
    print("Result:", result)

elif op == '-':
    result = a - b
    print("Result:", result)

elif op == '*':
    result = a * b
    print("Result:", result)

elif op == '/':
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")
