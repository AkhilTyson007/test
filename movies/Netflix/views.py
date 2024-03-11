from django.shortcuts import render, redirect
from django.http import HttpResponse
from Netflix.models import Student, Employee

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def salaar(request):
    return render(request, 'django.html')

def testing(request):
    return render(request, 'test.html')

def func(request):
    return render(request, 'about.html')


def add(request):
    return render(request, 'add.html')


def result(request):
    d= {'res': 'No Input Provided'}
    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        d = {'res': int(num1)+int(num2)}
    return render(request, 'result.html', d)



from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='signin')
def studDetails(request):
    if request.method=="POST":
        if request.POST.get('Display'):
            data = Student.objects.all()
            return render(request, "studDetails.html", {'data':data})
        f_name = request.POST['name']
        f_age = request.POST['age']
        f_email = request.POST.get('email')
        f_mobile = request.POST.get('mobile')
        Student.objects.create(name=f_name,age=f_age,email=f_email, mobile=f_mobile)
        
    print(request.user.id, request.user.is_staff)
  
    return render(request, "studDetails.html")


def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        empID = request.POST.get('empID')
        confirm_password = request.POST.get('confirm_password')
        if password==confirm_password:
            person = User.objects.create_user(username=username, password=password)
            Employee.objects.create(mobile=mobile,empID=empID, uid_id = person.id)
            messages.info(request,"Registration Successful! You can login now.")
            return redirect('signin')
        else:
            messages.info(request,'Passwords do not match. Please try again.')
            return redirect('register')
    return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'You are successfully logged in. Welcome {username}')
            return redirect('studDetails')
        else:
            messages.info(request, 'Username or Password is incorrect.Please try again.')
            return redirect('signin')
    return render(request,"signin.html")

def signout(request):
    messages.info(request, 'You have been logged out successfully.')
    logout(request)
    return redirect('signin')





