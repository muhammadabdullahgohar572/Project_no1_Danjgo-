from django.shortcuts import render
from .models import Tweet
from .forms import TweetFrom
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
def index(request):
    return render(request, "index.html")


def Tweet_list(request):
    tweet = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet_list.html", {"tweet": tweet})


def tweet_created(request):
    if request.method == "POST":
        form = TweetFrom(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = Tweet.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetFrom()
    return render(request, "tweet_form.html", {"form": form})


def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetFrom(request.POST, request.FILES)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = Tweet.user
        tweet.save()
        return redirect("tweet_list")
    else:
        form = TweetFrom()
    return render(request, "tweet_form.html", {"form": form})


def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect("tweet_list")
    else:
      return render(request, "tweet_confirm_delete.html", {"form": form})
