def calculate_total(*numbers):
    """
    Accepts any number of arguments (*args) and returns their sum.
    """
    total = 0
    for num in numbers:
        total += num
    return total

# --- Testing the function ---
# 1. Calling with 3 arguments
result1 = calculate_total(10, 20, 30)
print(f"Total of 10, 20, 30 is: {result1}")

# 2. Calling with 5 arguments
result2 = calculate_total(5, 5, 5, 5, 5)
print(f"Total of five 5s is: {result2}")

# 3. Calling with mixed floating point numbers
result3 = calculate_total(1.5, 2.5, 4.0)
print(f"Total of 1.5, 2.5, 4.0 is: {result3}")
