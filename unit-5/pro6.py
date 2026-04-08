cursor.execute("DELETE FROM students WHERE rollno=?", (1,))
conn.commit()