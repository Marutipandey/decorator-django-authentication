from django.shortcuts import render,redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .decorators import login_required_custom

@login_required_custom
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return HttpResponse("Invalid credentials", status=401)
    
    return render(request, 'enroll/login.html')
