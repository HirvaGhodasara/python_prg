# 1. Define the 4 Lambda functions for arithmetic operations
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Error: Division by Zero"

def main():
    try:
        # 2. Accept inputs from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        # 3. Check the operator and invoke the corresponding lambda function
        if operator == '+':
            result = addition(num1, num2)
            print(f"Result: {result}")
            
        elif operator == '-':
            result = subtraction(num1, num2)
            print(f"Result: {result}")
            
        elif operator == '*':
            result = multiplication(num1, num2)
            print(f"Result: {result}")
            
        elif operator == '/':
            result = division(num1, num2)
            print(f"Result: {result}")
            
        else:
            print("Invalid Operator selected.")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    main()
