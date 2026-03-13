def main():
    # Initialize an empty list
    my_list = []

    while True:
        # Display Menu Options
        print("\n--- LIST OPERATIONS MENU ---")
        print("1. Append (Add element to end)")
        print("2. Insert (Add element at specific index)")
        print("3. Remove (Delete specific element)")
        print("4. Pop (Delete element at specific index)")
        print("5. Sort List")
        print("6. Reverse List")
        print("7. Display List")
        print("8. Exit")
        print("----------------------------")

        # Get user choice
        choice = input("Enter your choice (1-8): ")

        # 1. Append
        if choice == '1':
            item = input("Enter element to append: ")
            my_list.append(item)
            print(f"'{item}' added to the list.")

        # 2. Insert
        elif choice == '2':
            item = input("Enter element to insert: ")
            try:
                index = int(input(f"Enter index (0 to {len(my_list)}): "))
                my_list.insert(index, item)
                print(f"'{item}' inserted at index {index}.")
            except ValueError:
                print("Error: Index must be an integer.")

        # 3. Remove (by value)
        elif choice == '3':
            item = input("Enter element to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"'{item}' removed from list.")
            else:
                print("Error: Element not found in list.")

        # 4. Pop (by index)
        elif choice == '4':
            if len(my_list) > 0:
                try:
                    index = int(input(f"Enter index to pop (0 to {len(my_list)-1}): "))
                    popped_item = my_list.pop(index)
                    print(f"'{popped_item}' popped from index {index}.")
                except (ValueError, IndexError):
                    print("Error: Invalid index.")
            else:
                print("List is empty. Nothing to pop.")

        # 5. Sort
        elif choice == '5':
            my_list.sort()
            print("List sorted successfully.")

        # 6. Reverse
        elif choice == '6':
            my_list.reverse()
            print("List reversed successfully.")

        # 7. Display
        elif choice == '7':
            print("\nCurrent List:", my_list)

        # 8. Exit
        elif choice == '8':
            print("Exiting program...")
            break

        # Invalid Input
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

# Run the program
if __name__ == "__main__":
    main()
