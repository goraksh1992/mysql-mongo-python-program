
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['testdatabase']
mycol = mydb['employee']

# result = mycol.find_one() # show only one record
  #  print(result)

# for result in mycol.find(): # show all records
  #  print(result)

# for result in mycol.find({},{"_id": 1, "address": 1}): # show only specific records
#     print(result)

#------------------------------------#
# cond = {"name": "John"}

# for result in mycol.find(cond): # where condition
#     print(result)
#------------------------------------#

#------------------------------------#
# show records name start with J

# cond = {"name": {"$gt": "J"}}

# for result in mycol.find(cond):
#     print(result)

#-------------------------------------#

#-------------------------------------#
# show records by order

for result in mycol.find().sort("_id", 1): # 1 for asc & -1 for desc
    print(result)
#-------------------------------------#



# for x in result:
#     print(x) 
  