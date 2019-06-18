import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

sql = 'DELETE FROM students WHERE name = "Rachel"'

mycursor.execute(sql)

mydb.commit()




