from django.shortcuts import get_object_or_404, render
from utils.migration import get_mongodb
from .models import Author #, Tag, Quote
# Create your views here.
db = get_mongodb()

def main(request):    
    quotes = db.quotes.find() # {'id': a, 'tags': [], author: a, fullname: a, born_date: datetime, born_location: a, description}
    return render(request, 'quotes/index.html', context={'quotes':quotes})

def author_info(request, slug_author):
    author = db.authors.find_one({'fullname':slug_author})
    return render(request, 'quotes/author_info.html', context={"author": author})

