from django import forms
from .models import Book, IssueRecord
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'total_quantity','available_quantity']

class IssueForm(forms.ModelForm):
    class Meta:
        model = IssueRecord
        fields = ['book']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
