
import db_connection

mycurser = db_connection.mycurser
mydb = db_connection.mydb

sql = "UPDATE employee SET name = %s WHERE address = %s"
val = ("Goraksh","pune")

mycurser.execute(sql, val)

mydb.commit()

print(mycurser.rowcount, "record updated") # show update record count