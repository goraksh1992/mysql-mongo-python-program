
import db_connection

mycurser = db_connection.mycurser
mydb = db_connection.mydb

# sql = "SELECT * FROM employee"

# used sql injection 

sql = "SELECT * FROM employee WHERE name = %s"
cndtn = ("Goraksh",) 

mycurser.execute(sql, cndtn)

result = mycurser.fetchall() # fetch all expected rows

# result = mycurser.fetchone() # fetch only one row

for record in result:
    print(record)

