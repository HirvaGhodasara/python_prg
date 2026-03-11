def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator"

Sum1 = float(input("Enter first number: "))
Sum2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = calculate(a, b, op)
print("Result:", result)
