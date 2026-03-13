# Program 2: User Defined Exception

class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise AgeError("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")

except AgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter a number.")
