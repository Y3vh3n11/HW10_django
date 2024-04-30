from django.shortcuts import render
from utils.migration import get_mongodb

from .models import Author, Tag, Quote
# Create your views here.

def main(request):
    # db = get_mongodb()
    # quotes = db.quotes.find() # {'id': a, 'tags': [], author: a, fullname: a, born_date: datetime, born_location: a, description}
    # session1 = session
    # def select_01():
# select s.id, s.fullname, AVG(g.grade) as avg_grade
# from students s
# join grades g 
# join grades g on s.id = g.student_id
# group by s.id
# order  by avg_grade desc 
# limit 5;
    quotesdick = {}
    quotes = Quote.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    for quote in quotes:        
        print(quote.quote)
        print(quote.author.fullname)
        print(quote.)

    return render(request, 'quotes/index.html', context={'quotes':quotesdick})