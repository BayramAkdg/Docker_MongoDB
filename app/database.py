from pymongo import MongoClient
import os

class Database:
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        """Connect to the MongoDB database."""
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/library")
        self.client = MongoClient(mongo_uri)
        self.db = self.client.get_database()

    def close(self):
        """Close the database connection."""
        if self.client:
            self.client.close()
