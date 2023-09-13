from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

# Create your views here.
def home(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('home')
        else:
            messages.error(request,"Authentication failed")
            return redirect('home')
    else:
        return render(request,"home.html",{})

def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')