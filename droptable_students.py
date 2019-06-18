import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

sql = 'DROP TABLE IF EXIST students'

mycursor.execute(sql)

mydb.commit()




