from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Employee
from .forms import AddEmployeeForm

# Create your views here.
# Home/Login page
def home(request):

    employees = Employee.objects.all()

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
        return render(request,"home.html",{'employees': employees})

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
    
# Add employee
def add_employee(request):
    form = AddEmployeeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST)
            if form.is_valid():
                form.save()
                messages.error(request,"Employee added successfully..")
                return redirect('home')
        else:
            return render(request,"add_employee.html",{'form': form})
    else:
        messages.error(request,"Login to see this page..")
        return redirect('home')

def delete_employee(request,id):
    if request.user.is_authenticated:
        employee_to_delete = Employee.objects.get(id=id)
        employee_to_delete.delete()
        messages.error(request,"Deleted successfully..")
        return redirect('home')
    else:
        messages.error(request,"Login to see this page..")
        return redirect('home')

def update_employee(request,id):
    print("Coming here...........")
    if request.user.is_authenticated:
        employee = Employee.objects.get(id=id)
        print(employee) 
        form = AddEmployeeForm(request.POST or None, instance=employee)
        if form.is_valid():
            form.save()
            messages.error(request,"Employee update successfully..")
            return redirect('home')
        else:
            print("***************************")
            return render(request, 'update_employee.html', {'form':form})
    else:
        messages.error(request,"Login to see this page..")
        return redirect('home')

def get_employee(request,id):
    if request.user.is_authenticated:
        employee = Employee.objects.get(id=id)
        return render(request,"employee.html",{'employee': employee})
    else:
        messages.error(request,"Login to see this page..")
        return redirect('home')

