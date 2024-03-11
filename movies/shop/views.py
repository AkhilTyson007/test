from django.shortcuts import render, redirect
from shop.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def register(request):
    if request.method=='POST':
        pub_date = request.POST.get('pub_date')
        product_type = request.POST.get('product_type')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        Product.objects.create(pub_date=pub_date, product_type=product_type, image=image, video=video)
        messages.info(request,"Registration Successful! You can login now.")
        return redirect('signin')
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






def mediaData(request):
    data = Product.objects.all()
    return render(request, 'test.html', {'records' : data})