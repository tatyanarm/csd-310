from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.mj8httk.mongodb.net/?retryWrites=true&w=majority")
db = client.pytech
try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
client.close()
