cursor.execute("UPDATE students SET age=? WHERE rollno=?", (23, 1))
conn.commit()