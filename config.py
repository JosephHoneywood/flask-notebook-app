import os
import pymongo
import dns

basedir = os.path.abspath(os.path.dirname(__file__))

client = pymongo.MongoClient("mongodb+srv://admin:Invba6JgyoEnDOLL@honeywood-azure.szwlj.mongodb.net/notebooks_db?retryWrites=true&w=majority")
db_mongo = client.get_database('notebooks_db')