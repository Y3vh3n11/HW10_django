from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AuthorForm
from utils.migration import get_mongodb
from django.contrib.auth.decorators import login_required
# Create your views here.
db = get_mongodb()

def main(request):    
    quotes = db.quotes.find() # {'id': a, 'tags': [], author: a, fullname: a, born_date: datetime, born_location: a, description}
    return render(request, 'quotes/index.html', context={'quotes':quotes})

def author_info(request, slug_author):
    author = db.authors.find_one({'fullname':slug_author})
    return render(request, 'quotes/author_info.html', context={"author": author})

@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            db.authors.insert_one({'fullname':form.cleaned_data['fullname'], 
            'born_date':form.cleaned_data['born_date'],
            'born_location':form.cleaned_data['born_location'],
            'description':form.cleaned_data['description']})
            
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/author.html', {'form': form})
    else:
        return render(request, 'quotes/author.html', {'form': AuthorForm()})