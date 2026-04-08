import sqlite3
import re

# Connect to database
conn = sqlite3.connect('student_data.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                  (rollno INTEGER PRIMARY KEY, name TEXT, gender TEXT, 
                   age INTEGER, email TEXT, mobile TEXT, city TEXT)''')
conn.commit()