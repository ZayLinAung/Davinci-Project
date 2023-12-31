import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *

def index(request):
    return render(request, 'ourProject/index.html')

def begin(request):
    return render(request, 'ourProject/Sign-up-(Year).html')

def firstYear(request):
    return render(request, 'ourProject/firstYear.html')

def academics(request):
    return render(request, 'ourProject/Academics.html')

def profilePage(request):
    return render(request, 'ourProject/ProfilePage.html')

def about(request):
    return render(request, 'ourProject/About.html')

def contact(request):
    return render(request, 'ourProject/Contact.html')

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
            return render(request, "ourProject/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "ourProject/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create(username = username, email = email, password = password)
            user.save()
        except IntegrityError:
            return render(request, "ourProject/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ourProject/register.html")