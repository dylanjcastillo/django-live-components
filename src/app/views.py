# views.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string

from app.models import Tweet


def index(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "index.html", {"tweets": tweets})


@require_POST
def post_tweet(request):
    content = request.POST.get("content")
    print(request.POST)
    if content:
        tweet = Tweet.objects.create(user=request.user, content=content)
        tweet_html = render_to_string("tweet.html", {"tweet": tweet})
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "tweet_updates",
            {
                "type": "tweet",
                "html": tweet_html,
            },
        )
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
