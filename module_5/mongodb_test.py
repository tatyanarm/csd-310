 #Import MongoClient
from pymongo import MongoClient
 #Creating variable Url and assign string from Atlas whit username and password 
url = ("mongodb+srv://admin:admin@cluster0.mj8httk.mongodb.net/?retryWrites=true&w=majority")
 #Variable whit client and calling MongoClient passing in bariable Url 
client = MongoClient(url)
 #Creating Variable and assign Database Instance 
db = client.pytech
 #Print Statemant if Datatabase Variable
print(db.list_collection_names())
 #Wait for User Imput
endprocess = input('End of program, Press any key to exit...')
print (endprocess)
