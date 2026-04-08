cursor.execute("SELECT * FROM students")
regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
for row in cursor.fetchall():
    if re.search(regex, row[4]):
        print(row)