import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser')

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdb")


