roll = input("Enter Roll No to search: ")
cursor.execute("SELECT * FROM students WHERE rollno=?", (roll,))
student = cursor.fetchone()
print(student if student else "Student not found.")