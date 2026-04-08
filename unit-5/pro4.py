cursor.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?)", (1, 'Nitin', 'M', 22, 'a@b.com', '9999999999', 'Rajkot'))
conn.commit()