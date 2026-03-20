class Student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.address = self.Address()   

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        self.address.display_address()

    class Address:
        
        def __init__(self):
            self.city = input("Enter City: ")
            self.state = input("Enter State: ")

        def display_address(self):
            print("City:", self.city)
            print("State:", self.state)


s1 = Student("Visha", 47)

s1.display()
