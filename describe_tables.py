import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE students")

for db in mycursor:
    print(db)




