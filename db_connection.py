import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "system",
    database = "mydatabase" 
)

mycurser = mydb.cursor()