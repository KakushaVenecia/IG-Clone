from operator import is_not
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login, logout


# Create your views here.
def landing(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Login Successful")
                return redirect('timeline')
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    form=AuthenticationForm                    
    return render(request, 'landing.html',{"form":form} )

def register(request):
    if request.method=='POST':
        form =newUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('landing')
        messages.error(request, 'Registration Failure')
    form=newUserForm()

    return render(request, 'signup.html', {"register_form":form})



def timeline(request):
    return render(request, 'timeline.html')

def profile(request):
    return render(request, 'profile.html')

def logout(request):
    logout(request)
    messages.success(request, "See you Soon!")
    return redirect('landing')
    
