# Program 8: Student marks processing

students = [
    "1,John,80,70,90,85",
    "2,Alice,60,75,65,70"
]

for line in students:
    data = line.split(",")

    roll = data[0]
    name = data[1]
    marks = list(map(int, data[2:]))

    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\nRoll No:", roll)
    print("Name:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("----------------------")
