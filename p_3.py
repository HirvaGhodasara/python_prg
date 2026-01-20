# Program to calculate total, percentage and grade

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))

total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Grade: A")

elif percentage >= 60:
    print("Grade: B")

elif percentage >= 50:
    print("Grade: C")

elif percentage >= 40:
    print("Grade: D")

else:
    print("Grade: Fail")
