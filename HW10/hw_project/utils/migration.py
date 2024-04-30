import configparser
import os
import django
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import sys


sys.path.append(os.path.abspath('..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_project.settings')
django.setup()

from quotes.models import Quote, Tag, Author 
def get_mongodb():
    # config = configparser.ConfigParser()
    # config.read('config.ini')

    # mongo_user = config.get('DB', 'user')
    # mongodb_pass = config.get('DB', 'pass')
    # db_name = config.get('DB', 'db_name')
    # domain = config.get('DB', 'domain')

    mongo_user = 'codepraktik'
    mongodb_pass = 'it9AktJTWuXbqazI'
    db_name = 'HW10'
    domain = 'cluster0.esxaixs.mongodb.net'

    uri = f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority'

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.HW10

    return db

def migration():
    db = get_mongodb()
    authors = db.authors.find()

    for author in authors:
        Author.objects.get_or_create(
            fullname=author['fullname'],
            born_date=author['born_date'],
            born_location=author['born_location'],
            description=author['description'],
        )

    quotes = db.quotes.find()
    a = 0
    for quote in quotes:
        tags = []
        for tag in quote['tags']:
            # t, *_ = Tag.objects.get_or_create(name=tag)
            tags.append(tag)
        
        exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

        if not exist_quote:  
            author = db.authors.find_one({'fullname':quote['author']['fullname']})
            a = Author.objects.get(fullname=author['fullname'])
            q = Quote.objects.create(quote=quote['quote'], author=a)
            for tag in tags:
                q.tags.add(tag)

if __name__ == '__main__':
    migration()