### Import a database module
import mysql.connector

### Establish a database connection
con=mysql.connector.connect(
    user="root",
    password="password",
    host="localhost",
    database = "mydb"
)
print("Successfully connected!")

#Setup variables
# productID=4
# productName='LEMONTEA'

### Create a cursor object to run SQL queries
cursor = con.cursor()

### Insert data
#cursor.execute("INSERT INTO product(id, name) VALUES (%s,%s)",(productID, productName))

### Update data
#data = cursor.fetchone() #Only retrieve one row of data; fetchall(): get all of the data
#1st method: 
#cursor.execute("UPDATE product SET name='AMERICANO COFFEE' WHERE id=1")

#2nd method: 
# productName= "AMERICANO"
# productID=1
# cursor.execute("UPDATE product SET name=%s WHERE id=%s", (productName,productID))

### Fetch one row of data
# cursor.execute("SELECT * FROM product WHERE id=2")
# data=cursor.fetchone() # Only retrieve one row of data
# print(data) # Print all at once
# print(data[0], data[1]) # Print out separately

### Fatch multipls rows of data
cursor.execute("SELECT * FROM product")
data=cursor.fetchall(); 
#print(data)
for row in data: 
    print(row[0],row[1])


###Execute this task
con.commit() 
###Close the connection when done
con.close(); 