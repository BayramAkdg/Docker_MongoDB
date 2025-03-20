from pymongo import MongoClient

class Database:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="library"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["books"]

    def insert(self, data):
        self.collection.insert_one(data)

    def find_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def update(self, filter_query, new_values):
        self.collection.update_one(filter_query, {"$set": new_values})

    def delete(self, filter_query):
        self.collection.delete_one(filter_query)

    def close(self):
        self.client.close()
