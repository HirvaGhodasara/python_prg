# Program 5: Read content and count words (without external file)

content = """Python is easy to learn
Python is powerful"""

print("File Content:\n")
print(content)

words = content.split()
print("\nTotal number of words:", len(words))
