from django.shortcuts import render

# Create your views here.
def all_tweets(request):
    return render(request, 'tweets_home.html')