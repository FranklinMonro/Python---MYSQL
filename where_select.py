import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

sql = 'SELECT * FROM students WHERE name LIKE "Fr%"'

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)




