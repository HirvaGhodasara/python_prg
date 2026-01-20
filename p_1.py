# Program to calculate Simple Interest

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
n = float(input("Enter the time (in years): "))

si = (p * r * n) / 100

print("Simple Interest is:", si)
