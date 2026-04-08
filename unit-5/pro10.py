while True:
    print("\n1. Insert 2. Update 3. Search 4. Delete 5. List 6. Exit")
    choice = input("Choice: ")
    if choice == '1':
        # Prompt for details and cursor.execute("INSERT...")
        pass
    elif choice == '5':
        cursor.execute("SELECT * FROM students")
        print(cursor.fetchall())
    elif choice == '6':
        break