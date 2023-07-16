    #Import MongoClient
from pymongo import MongoClient
    #Creating variable Url and assign string from Atlas whit username and password 
url = ("mongodb+srv://admin:admin@cluster0.mj8httk.mongodb.net/?retryWrites=true&w=majority")
    #Variable whit client and calling MongoClient passing in bariable Url 
client = MongoClient(url)
    #Creating Variable and assign Database Instance 
db = client.pytech
    #Print Statemant if Datatabase Variable
mycollection =db["students"]

myquery = {"Student_ID" : "1007" }
newvalues = {"$set": {"Last_Name": "Golum"}}
mycollection.update_one(myquery, newvalues)   

#print "customers" after the update:
for x in mycollection.find({'Student_ID': 1007}):
  print(x)
