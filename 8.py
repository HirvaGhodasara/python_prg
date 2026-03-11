a = input("Enter a String: ")

# a) Count vowels
vowel = ('a','e','i','o','u','A','E','I','O','U')
count = 0
for i in a:
    if i in vowel:
        count = count + 1
print("Number of vowels:", count)

# b) Length of string (without len)
length = 0
for i in a:
    length = length + 1
print("Length of string:", length)

# c) Reverse string
reverse = ""
for i in a:
    reverse = i + reverse
print("Reversed string:", reverse)

# d) Find and replace
find = input("Enter character to find: ")
replace = input("Enter character to replace: ")
new = a.replace(find, replace)
print("After replace:", new)

# e) Palindrome check
if a == reverse:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")
