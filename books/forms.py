from django import forms
from .models import Book, Publisher


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {'title', 'desc', 'ISBN'}


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = {'name', 'email'}
