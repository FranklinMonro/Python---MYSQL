import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()
sqlINSERT = 'INSERT INTO students(name, age) VALUES (%s, %s)'
student1 = ("Rachel",22)

mycursor.execute(sqlINSERT, student1)

mydb.commit()




