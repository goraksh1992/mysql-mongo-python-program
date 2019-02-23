
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2701/")

# database select
mydb = myclient['testdatabase']
mycol = mydb["employee"]
