
# to render the html file
from django.shortcuts import render

# to get the Tweet model
from .models import Tweet

# to get the TweetForm
from .forms import TweetForm

# to get the object from the database or return 404 error
from django.shortcuts import get_object_or_404 , redirect



# Create your views here.

# to get all the tweets from the database and render them in the tweets_home.html file 
# def all_tweets(request):
#     return render(request, 'tweets_home.html')


def tweet_list(request): 
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})



# create a new tweeet .. 
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user 
            tweet.save()
            return redirect('tweets:tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})



# edit tweet by the user 
def tweet_edit(request , tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user = request.user )
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets:tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})




# delete tweet by the user
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweets:tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})
