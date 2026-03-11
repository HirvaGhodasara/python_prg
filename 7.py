# Write a program to create a list and perform various operations on list using menu.


lst = []

while True:
    print("\nMENU")
    print("1. Add element")
    print("2. Remove element")
    print("3. Display list")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to add: "))
        lst.append(value)
        print("Element added")

    elif choice == 2:
        value = int(input("Enter value to remove: "))
        if value in lst:
            lst.remove(value)
            print("Element removed")
        else:
            print("Element not found")

    elif choice == 3:
        print("List elements:", lst)

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
