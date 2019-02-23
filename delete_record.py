
import db_connection

mycurser = db_connection.mycurser
mydb = db_connection.mydb

name = input("Enter name to delete : ")

# sql = "DELETE FROM employee WHERE name = 'gaurav'" # we directly use this

sql = "DELETE FROM employee WHERE name = %s"
# cndtn = ("gaurav",) # sql injection
cndtn = (name,)

mycurser.execute(sql, cndtn)

mydb.commit()

print(mycurser.rowcount, "record deleted")
