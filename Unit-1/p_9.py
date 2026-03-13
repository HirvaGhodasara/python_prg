def calculate(num1, num2, operator):
    """
    Accepts two numbers and an operator to perform basic arithmetic.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Invalid Operator"

# --- Main Program ---
try:
    # Taking inputs from user
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    op = input("Enter operator (+, -, *, /, %): ")

    # Calling the function
    result = calculate(n1, n2, op)

    # Displaying the result
    print(f"\nResult: {n1} {op} {n2} = {result}")

except ValueError:
    print("Invalid input! Please enter numeric values for numbers.")
