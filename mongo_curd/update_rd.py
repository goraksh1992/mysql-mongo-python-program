
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['testdatabase']
mycol = mydb['employee']

cond = {"name" : "John"}
newValue = {"$set": {"name": "Gaurav", "address": "Pune"}}

# mycol.update_one(cond,newValue) # update only one record

mycol.update_many(cond,newValue) # update only all match record

for result in mycol.find():
    print(result)