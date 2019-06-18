import mysql.connector

conn = mysql.connector.connection(host = 'localhost', user = 'myuser', password = 'myuser', database = 'student_db')
cursor = conn.cursur()
cursor.execute("SELECT * FROM java_prog")
rows = cursor.fetchall()
for eachRow in rows:
    print(eachRow)
