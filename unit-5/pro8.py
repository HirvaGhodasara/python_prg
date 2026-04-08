cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    name = row[1]
    if name.startswith('N') and len(name) == 5:
        print(row)