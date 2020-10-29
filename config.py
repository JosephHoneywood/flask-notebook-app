import os
import pymongo
import dns

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

client = pymongo.MongoClient("mongodb+srv://admin:Invba6JgyoEnDOLL@honeywood-azure.szwlj.mongodb.net/notebooks_db?retryWrites=true&w=majority")
db_mongo = client.get_database('notebooks_db')