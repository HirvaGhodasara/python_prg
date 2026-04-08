columns = [('name', 'varchar', 20), ('qualification', 'varchar', 20), 
           ('post', 'varchar', 20), ('salary', 'int', 6)]

query = "CREATE TABLE employees ("
for col in columns:
    query += f"{col[0]} {col[1]}({col[2]}), "
query = query.rstrip(', ') + ")"
cursor.execute(query)