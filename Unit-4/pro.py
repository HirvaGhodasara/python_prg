import pandas as pd

data = {
    'RollNo': range(101, 121),
    'Name': [f'Student {i}' for i in range(1, 21)],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'] * 4,
    'E-Mail': ['test@gmail.com', 'invalid-email', 'user@yahoo.com', 'abc@domain.in', 'wrong@com'] * 4,
    'Mobile': ['91-9876543210', '9876543211', '91-1234567890', '8888888888', '91-5555544444'] * 4,
    'Age': [19, 21, 22, 18, 25, 20, 23, 19, 24, 21, 22, 18, 19, 20, 21, 22, 23, 24, 25, 20],
    'City': ['Rajkot', 'Surat', 'Rajkot', 'Ahmedabad', 'Baroda', 'Rajkot', 'Mumbai', 'Rajkot', 'Surat', 'Ahmedabad'] * 2
}

df_initial = pd.DataFrame(data)
df_initial.to_excel('students.xlsx', index=False)
print("Excel file 'students.xlsx' created successfully.")