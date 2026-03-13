# Program 3:

import logging

# Configure logging
logging.basicConfig(
    filename="error_log.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError as e:
    print("Arithmetic Exception occurred!")
    logging.error("Division by zero error occurred")

except ValueError:
    print("Please enter valid numbers.")
