import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'testdb')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students LIMIT 5")
myresult = mycursor.fetchall()
for result in myresult:
    print(myresult)






