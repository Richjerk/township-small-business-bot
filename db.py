# db.py
import pymongo
from pymongo import MongoClient

# Replace the following with your MongoDB Atlas connection string
MONGODB_URI = "mongodb://atlas-sql-64cf1e5950ebbc37fa7eee8e-icpps.a.query.mongodb.net/ShopLocal-Assistant?ssl=true&authSource=admin"

def get_database():
    client = MongoClient(MONGODB_URI)
    return client['mongodb://atlas-sql-64cf1e5950ebbc37fa7eee8e-icpps.a.query.mongodb.net/ShopLocal-Assistant?ssl=true&authSource=admin']

def get_users_collection():
    db = get_database()
    return db['users']

