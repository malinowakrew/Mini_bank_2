from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
try:
    mongoClient = MongoClient('mongodb://localhost:27017')
    #print(mongoClient.server_info())
except:
    raise ConnectionFailure

db = mongoClient['mini_bank']