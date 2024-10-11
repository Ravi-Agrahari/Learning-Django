from django.urls import path
from . import views

urlpatterns = [
    # path('', views.all_tweets, name='tweets'),
    path('', views.tweet_list, name='tweet_list'),
    path('new/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    
]
