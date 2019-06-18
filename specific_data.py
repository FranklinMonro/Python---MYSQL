import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

mycursor.execute("SELECT age FROM students")

myresult = mycursor.fetchall()
myresult2 = mycursor.fetchone()
for row in myresult:
    print(row)




