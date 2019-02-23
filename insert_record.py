
import db_connection

mycurser = db_connection.mycurser
mydb = db_connection.mydb

# get data from user
name = input("Enter the name : ")
address = input("Enter the address : ")

sql = "INSERT INTO employee (name, address) VALUES (%s, %s)"
# val = ("gaurav", "pune")
val = (name, address)

mycurser.execute(sql, val)

mydb.commit()

# print(mycurser.rowcount, "record inserted")
print("last insert ID : ", mycurser.lastrowid)
