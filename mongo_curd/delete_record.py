
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['testdatabase']
mycol = mydb['employee']

cond = {"name" : "John"}

# x = mycol.delete_one(cond) # delete only one record

x = mycol.delete_many(cond) # delete all match records

print(x.deleted_count, " records deleted")