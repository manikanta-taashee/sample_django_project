from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # return render(request, 'base.html', {})
    return redirect('login')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # print(request.user)
            # print(request.user.id)
            # #print(request.user.is_authenticated, request.user)
            return redirect('dashboard')
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'login.html', { 'passwordcheck': f"Password for '{username}' is Wrong.", 'username': username })
            else:
                return render(request, 'login.html', { 'usernamecheck': f"User with '{username}' Not Found.", 'username': username })
    return render(request, 'login.html', {})

def logout(request):
    auth_logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html', {"user": request.user})

def all_users(request):
    users_list = User.objects.all()
    return render(request, 'all_users.html', {"user": request.user, "users_list": users_list})
