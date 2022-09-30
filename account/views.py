from unicodedata import name
from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import RegisterDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password


def RegisterPage(request):
    form = RegisterForm()
    context = {'form':form}
    if request.method == 'POST':
        form1 = RegisterForm(request.POST) 
        if form1.is_valid():
            form1.password=make_password(request.POST['password'])
            form1.save()
            return redirect('register')
    return render(request,'register.html',context)

def LoginPage(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pswd = request.POST.get('password')
        user1 = authenticate(name=user,password=pswd)
        if user1 is not None:
            login(request,user1) 
            return redirect("profile")
        else:
            return redirect("login")
    return render(request,'login.html') 

#login_required(login_url='login')
def ProfilePage(request):
      return render(request,'profile.html')

def LogoutUser(request):
    logout(request)
    return redirect('login')
      
