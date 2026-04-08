# List of students from Rajkot City
rajkot_students = df[df['City'] == 'Rajkot']

# List of Male students
male_students = df[df['Gender'] == 'Male']

# List of Male students from Rajkot City
male_rajkot = df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')]

# List of students whose age >= 20
age_20_plus = df[df['Age'] >= 20]

print(male_rajkot) # Example output