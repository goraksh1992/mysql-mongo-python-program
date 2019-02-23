import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["testdatabase"]

mycol = mydb["employee"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print("last insrted ID : ", x.inserted_id)