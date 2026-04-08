import pandas as pd

df = pd.read_excel('students.xlsx')
print("Columns:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)