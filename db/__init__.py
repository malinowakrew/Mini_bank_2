from pymongo import MongoClient
mongoClient = MongoClient('mongodb://localhost:27017')
db = mongoClient['mini_bank']