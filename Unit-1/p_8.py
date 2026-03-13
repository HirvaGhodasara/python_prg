def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def get_length_manual(text):
    """Counts length without using len()"""
    count = 0
    for _ in text:
        count += 1
    return count

def reverse_string(text):
    # Uses slicing to reverse [start:end:step]
    return text[::-1]

def check_palindrome(text):
    # A string is a palindrome if it looks the same reversed
    # We remove spaces and convert to lower case for accurate comparison
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

def main():
    while True:
        print("\n--- String Operations Menu ---")
        print("1. Enter/Change String")
        print("a. Count Number of Vowels")
        print("b. Count Length of String (Manual)")
        print("c. Reverse String")
        print("d. Find and Replace")
        print("e. Check Palindrome")
        print("x. Exit")
        
        choice = input("\nEnter your choice: ").lower()

        if choice == 'x':
            print("Exiting program.")
            break
            
        if choice == '1':
            current_string = input("Enter a string: ")
            continue

        # Ensure string is entered before operations
        try:
            current_string
        except NameError:
            current_string = input("Please enter a string first: ")

        if choice == 'a':
            print(f"Number of vowels: {count_vowels(current_string)}")
        
        elif choice == 'b':
            print(f"Length of string: {get_length_manual(current_string)}")
        
        elif choice == 'c':
            print(f"Reversed string: {reverse_string(current_string)}")
        
        elif choice == 'd':
            find_text = input("Enter text to find: ")
            replace_text = input("Enter text to replace with: ")
            new_string = current_string.replace(find_text, replace_text)
            print(f"Modified string: {new_string}")
            # Optional: Update current string to the new version
            # current_string = new_string 
        
        elif choice == 'e':
            if check_palindrome(current_string):
                print("Yes, it is a palindrome.")
            else:
                print("No, it is not a palindrome.")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
