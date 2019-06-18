import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (name VARCHAR(255), AGE INT)")




