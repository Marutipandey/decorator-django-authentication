from django.shortcuts import render,redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from .decorators import login_required_custom

# @login_required_custom
def home(request):
    return render(request, 'enroll/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home') 
        else:
            return HttpResponse("Invalid credentials", status=401)
    
    return render(request, 'enroll/login.html')


# enroll/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import SignupForm  
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)  
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = SignupForm()  

    return render(request, 'enroll/signup.html', {'form': form})

def logout_view(request):
    logout(request) 
    return redirect('login')  
