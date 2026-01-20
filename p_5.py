# Program to find the largest odd number from 10 entered numbers

largest_odd = None

print("Enter 10 numbers:")

for i in range(10):
    num = int(input())
    
    if num % 2 != 0:  # check if number is odd
        if largest_odd is None or num > largest_odd:
            largest_odd = num

if largest_odd is not None:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd numbers were entered")
