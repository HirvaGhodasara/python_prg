# Program 10:

import zipfile

# Step 1: Create a sample file
file = open("sample_data.txt", "w")
file.write("This is a sample file for zip example.")
file.close()

# Step 2: Zip the file
with zipfile.ZipFile("compressed_file.zip", "w") as zipf:
    zipf.write("sample_data.txt")

print("File zipped successfully!")

# Step 3: Unzip the file
with zipfile.ZipFile("compressed_file.zip", "r") as zipf:
    zipf.extractall("unzipped_files")

print("File unzipped successfully!")
