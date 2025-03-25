from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetFrom(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']
    
    
class UserRegsisterForm(UserCreationForm):
   email= forms.EmailField()
   class Meta:
       model=User
       fields=("username","email","password1","password2")
        