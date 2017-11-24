#!flask/bin/python
from flask_pymongo import PyMongo,MongoClient

client = MongoClient('mongodb://localhost:27017/')
parcelsDb = client.restdb

parcels = {'id':1,
           'adress':'1fakestreet'
           }
parcelsDb.mytable.insert(parcels)
