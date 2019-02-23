import db_connection

mycurser = db_connection.mycurser
mydb = db_connection.mydb

# query for create table

mycurser.execute("CREATE TABLE employee (name varchar(20), \
address varchar(200))")
