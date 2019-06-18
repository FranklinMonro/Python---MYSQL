import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()
sqlINSERT = 'INSERT INTO students(name, age) VALUES (%s, %s)'
students = [("Franco",40),
            ("Nina",46),
            ("Wendy",42),
            ("Quintilla",36),
            ("Rita",48)]

mycursor.executemany(sqlINSERT, students)

mydb.commit()




