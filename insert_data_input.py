import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'librarydb')

mycursor = mydb.cursor()
bookID = int(input("Please enter the book ID: "))
bookTITLE = input("Pleaes enter the book TITLE: ")
bookAUTHOR = input("Pleae enter the book AUTHOR: ")
bookQTY = int(input("Pleae enter the book STOCK: "))
sqlINSERT = 'INSERT INTO books(id, title, author, qty) VALUES (%s,%s,%s,%s)'
bookINSERT =(bookID, bookTITLE, bookAUTHOR, bookQTY)
print("INSERT INTO books VALUES(" , bookID , "," , bookTITLE , "," , bookAUTHOR , "," , bookQTY , ")")

mycursor.execute(sqlINSERT, bookINSERT)

mydb.commit()




