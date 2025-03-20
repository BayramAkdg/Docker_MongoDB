from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://mongo:27017/")
    return client["library"], client

def close_connection(client):
    client.close()
