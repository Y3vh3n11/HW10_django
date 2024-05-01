from django.shortcuts import render
from utils.migration import get_mongodb

# Create your views here.

def main(request):
    db = get_mongodb()
    quotes = db.quotes.find() # {'id': a, 'tags': [], author: a, fullname: a, born_date: datetime, born_location: a, description}

    return render(request, 'quotes/index.html', context={'quotes':quotes})