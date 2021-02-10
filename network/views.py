from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Post
import datetime


# function that ensures that there's always a loged in user before rendering views 
def login_required(func):
    def wraper(request,*args,**kwargs):
        if not request.user.is_authenticated: return HttpResponseRedirect(reverse("login"))
        else: 
            x=func(request,*args,**kwargs)
            return x
    return wraper    

# get the current time when a user shares a new post 
def get_time_now():
    return datetime.datetime.now().strftime(f"%b. %m,%Y, %I:%M %p")


def index(request):
    if request.method=="POST":
    # creating new post  and save it  in the database: 
        content = request.POST.get("post_content")

        current_user=User.objects.get(pk=request.user.id)

        new_post = Post(content=content,user=current_user,time=get_time_now())
        new_post.save()
        return HttpResponseRedirect(reverse('index'))
    else :
    #quering the post from the database  
        all_posts = Post.objects.all().order_by("-id")

        return render(request, "network/index.html",{
        "posts":all_posts
    })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

#@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
