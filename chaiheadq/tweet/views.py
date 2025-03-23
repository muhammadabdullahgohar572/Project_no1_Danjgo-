from django.shortcuts import render
from .models import Tweet
from .forms import TweetFrom
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return render(request,'index.html')

def Tweet_list(request):
    Tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':Tweets})