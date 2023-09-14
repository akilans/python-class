from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
# Home/Login page
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

# logout page
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')

# Register User
def register_user(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully")
                return redirect('home')
            else:
                messages.error(request,"Authentication failed")
                return redirect('home')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = UserRegisterForm()
        return render(request,"register.html",{'form': form})