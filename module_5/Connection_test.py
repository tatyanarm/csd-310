 #Import MongoClient
from pymongo import MongoClient
#Creating variable Url and assign string from Atlas whit username and password 
client = MongoClient("mongodb+srv://admin:admin@cluster0.mj8httk.mongodb.net/?retryWrites=true&w=majority")
#Creating Variable and assign Database Instance
db = client.pytech
#Print Statemant if Datatabase connected
try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
#close client
client.close()
