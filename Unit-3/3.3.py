class Student:
    school_name = "ABC School"   

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

s1 = Student("Visha", 101)
s2 = Student("Ayush", 102)

s1.display()
s2.display()

print("\nSchool Name:", Student.school_name)

Student.change_school("XYZ School")

print("Updated School Name:", Student.school_name)
