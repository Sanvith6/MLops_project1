from pymongo import MongoClient

uri = "mongodb+srv://sanvithjs68:VWKmpd7iyaWi06Bf@cluster0.edgdscv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())  # will throw if it can't connect
except Exception as e:
    print("Connection error:", e)
