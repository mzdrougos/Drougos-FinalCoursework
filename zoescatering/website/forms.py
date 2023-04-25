from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProductReview


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReviewAdd(forms.ModelForm):
    class Meta:
        model=ProductReview
        fields=('review_text','review_rating')
