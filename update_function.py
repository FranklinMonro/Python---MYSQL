import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'myuser', password = 'myuser', database = 'librarydb')

mycursor = mydb.cursor()
bookID = int(input("Please give ID of book you want to change: "))
newBookID = int(input("Please enter new ID of book: "))
sqlUPDATE = 'UPDATE books SET id =' + str(newBookID) + ' WHERE id =' + str(bookID)
print(sqlUPDATE)
print(mycursor.execute(sqlUPDATE))
          
#sql = 'UPDATE books SET id = 95 WHERE id = 87'



mydb.commit()






