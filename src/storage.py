import pymongo
from pymongo import MongoClient

from src import MONGO_URL

client = MongoClient(MONGO_URL)

db = client.telegrambot
users = db.users

def add_user(user):
    return users.insert_one(user).inserted_iddef

def get_user_by_field(field, value):
    return users.find_one({ field: value})

def set_user_credentials(email, credentials):
    users.update(
        {"email": email},
        credentials
    )