from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tweet_list, name="tweet_list"),
    path("tweet_created", views.tweet_created, name="tweet_created"),
  path("<int:tweet_id>/edit/", views.tweet_edit, name="tweet_edit"),
 path("<int:tweet_id>/delete/", views.tweet_delete, name="tweet_delete"),
    path("register", views.Register, name="register"),
]
