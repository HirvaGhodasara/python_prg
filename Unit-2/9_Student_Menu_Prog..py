# Program 9: Student Menu Program

students = {}

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. List All Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        students[roll] = name
        print("Student Added Successfully.")

    elif choice == '2':
        roll = input("Enter Roll No to search: ")
        if roll in students:
            print("Student Name:", students[roll])
        else:
            print("Student not found.")

    elif choice == '3':
        print("All Students:")
        for roll, name in students.items():
            print(roll, "-", name)

    elif choice == '4':
        roll = input("Enter Roll No to update: ")
        if roll in students:
            name = input("Enter New Name: ")
            students[roll] = name
            print("Student Updated.")
        else:
            print("Student not found.")

    elif choice == '5':
        roll = input("Enter Roll No to delete: ")
        if roll in students:
            del students[roll]
            print("Student Deleted.")
        else:
            print("Student not found.")

    elif choice == '6':
        print("Exiting Program.")
        break

    else:
        print("Invalid choice!")
