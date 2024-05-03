import configparser
import os
import django
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import sys


sys.path.append(os.path.abspath('..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_project.settings')
django.setup()


def get_mongodb():
    # config = configparser.ConfigParser()
    # config.read('config.ini')

    # mongo_user = config.get('DB', 'USER')
    # mongodb_pass = config.get('DB', 'PASS')
    # db_name = config.get('DB', 'DB_NAME')
    # domain = config.get('DB', 'DOMAIN')

    mongo_user = 'codepraktik'
    mongodb_pass = 'it9AktJTWuXbqazI'
    db_name = 'HW10'
    domain = 'cluster0.esxaixs.mongodb.net'

    uri = f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority'

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.HW10

    return db