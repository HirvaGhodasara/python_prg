class Student:
    
    def AddStudent(self):
        self.rollno = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def DisplayStudent(self):
        print("\nStudent Details:")
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


# Create object
s1 = Student()

# Call methods
s1.AddStudent()
s1.DisplayStudent()
