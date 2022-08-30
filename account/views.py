from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from poll.models import *

# Create your views here.

def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User alresdy exists")
                print("User alresdy exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                user.save()
                c = Count_total_poll(current_user_name=user, total_polls=0)
                c.save()
                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            messages.error(request, "password do not match")
            return redirect('register')

    return render(request, 'account/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

    return render(request, 'account/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are successfully logout")

    return redirect('register')

@login_required(login_url='login')
def profile(request):
    questions = Poll.objects.filter(current_user_name=request.user)
    return render(request, 'account/profile.html', {'questions': questions})