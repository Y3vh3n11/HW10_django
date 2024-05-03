from django.forms import CharField, ModelForm, TextInput
from django import forms
from .models import Author

class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=30)
    born_location = CharField(min_length=3, max_length=80)
    description = CharField(min_length=3, required=True)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']