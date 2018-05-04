from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client.sample_db
collection = db.my_first_collection

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

result1 = collection.insert_one(post)

print(collection.find_one())