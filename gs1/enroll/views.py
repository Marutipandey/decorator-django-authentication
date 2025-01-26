from django.shortcuts import render,redirect

# Create your views here.

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .decorators import login_required_custom

# Home view that requires the user to be logged in
@login_required_custom
def home(request):
    return render(request, 'home.html')

# Login view to authenticate the user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            return HttpResponse("Invalid credentials", status=401)
    
    return render(request, 'login.html')
