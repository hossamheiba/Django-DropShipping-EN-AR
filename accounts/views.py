from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import signupform
from django.contrib.auth import authenticate, login , logout
from .models import Profile


def signup(requset):
    if requset.method == "POST":
        form = signupform(requset.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(requset, user)
            return redirect("/")
    else:
        form = signupform()
    return render(requset, "registration/signup.html", {'form': form})


def signout(request):
    logout(request)
    return redirect('/')
