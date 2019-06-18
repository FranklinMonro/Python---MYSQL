import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

sql = 'UPDATE students SET age = 39 WHERE name = "Franco"'

mycursor.execute(sql)

mydb.commit()






