cursor.execute("SELECT * FROM students")
while True:
    row = cursor.fetchone()
    if row is None: break
    print(row)