# Program to display Armstrong numbers from 10 entered numbers

print("Enter 10 numbers:")

for i in range(10):
    num = int(input())
    temp = num
    digits = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** digits)
        temp = temp // 10

    if sum == num:
        print(num, "is an Armstrong number")
