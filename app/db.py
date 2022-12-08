from pymongo import MongoClient

cliente=MongoClient('localhost',27017)

db=cliente['api_proyecto']  #base de datos