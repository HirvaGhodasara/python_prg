cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)