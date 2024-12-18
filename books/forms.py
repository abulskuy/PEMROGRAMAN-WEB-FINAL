# books/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must be numeric.")
        return isbn