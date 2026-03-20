class Student:
    def show_student(self):
        print("This is Student class")

class Course:
    def show_course(self):
        print("This is Course class")

class Result(Student, Course):
    def show_result(self):
        print("This is Result class")

r1 = Result()

r1.show_student()
r1.show_course()
r1.show_result()

print("\nMRO of Result class:")
for i in Result.__mro__:
    print(i)
