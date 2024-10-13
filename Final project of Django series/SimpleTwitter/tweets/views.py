
# to render the html file
from django.shortcuts import render

# to get the Tweet model
from .models import Tweet

# to get the TweetForm
from .forms import TweetForm , UserRegistrationForm

# to get the object from the database or return 404 error
from django.shortcuts import get_object_or_404 , redirect

# to create login functionality in project 
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login



# Create your views here.

# to get all the tweets from the database and render them in the tweets_home.html file 
# def all_tweets(request):
#     return render(request, 'tweets_home.html')


def tweet_list(request): 
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})



# create a new tweeet ..
@login_required 
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
@login_required
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
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweets:tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


#view for registering the user ... 
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return request('tweet_list')

        
    else :
        form = UserRegistrationForm()
     
    return render(request, 'registration/register.html', {'form': form})