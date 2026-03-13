# Create a module with 4 functions of your choice. Import and use the functions using module in different ways.
# ----- Module Code -----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# ----- Using functions in different ways -----

# Method 1: Using module name (simulated)
import sys
this_module = sys.modules[__name__]

print("Method 1:")
print(this_module.add(10, 5))
print(this_module.subtract(10, 5))

# Method 2: Import specific functions (simulated)
from __main__ import multiply, divide

print("Method 2:")
print(multiply(10, 5))
print(divide(10, 5))

# Method 3: Import with alias (simulated)
import __main__ as mm

print("Method 3:")
print(mm.add(20, 10))
print(mm.divide(20, 4))

# Method 4: Import all (simulated)
from __main__ import *

print("Method 4:")
print(add(15, 5))
print(subtract(15, 5))
