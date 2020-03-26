from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def log_in(request):
    if request.method == 'POST':
        print(request.POST)
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            print(user)
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('login')

    # if request.method == 'POST':
    #     print(request.POST)
    #     user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
    #     if user is not None:
    #         print(user)
    #         login(request,user)
    #         return redirect('home')
    #     else:
    #         messages.error(request,'username or password not correct')
    #         return redirect('login')