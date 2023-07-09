from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib import messages
from accounts.models import CustomUser
from accounts.otp import *

# Create your views here.

@never_cache
def UserSingup(request):
    if request.user.is_authenticated:
        return redirect('settings')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                if CustomUser.objects.filter(email=email).exists():
                    messages.info(request,'Email already Registered. Please log in.')
                    return redirect('user-signup')
                elif CustomUser.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exists.')
                    return redirect('user-signup')
                else:
                    user = CustomUser.objects.create_user(username=username, email=email, password=password)
                    user.is_active = True
                    user.save()
                    login(request, user)
                    return redirect('settings')
                    # send_otp(user.email)
                    # request.session['email']=user.email
                    # return redirect('otp-verify')
            else:
                messages.info(request, 'Invalid Entry')
                return redirect('user-signup')
        else:
            return render(request, 'auth/Signup.html')

@never_cache
def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('settings')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)    
            if user is not None:
                login(request, user)
                return redirect('settings')
            else:
                if CustomUser.objects.filter(is_active = False):
                    messages.info(request, 'Your Account has been Suspended')
                    return redirect('user-login')
                else:
                    messages.error(request, 'Invalid Username or Password')
                    return redirect('user-login')
        else:
            return render(request, 'auth/Login.html')
        
@never_cache
def otp_verify(request):
    if request.user.is_authenticated:
        return redirect('settings')
    else:
        email=request.session['email']
        print(email, 'in session')
        if request.method == "POST":
            email=request.session['email']
            user= CustomUser.objects.get(email=email)
            code = request.POST.get('code')
            check = verify_otp(email, code)
            if check:
                user.is_active = True
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid OTP')
                return redirect('otp-verify')
        else:
            return render(request, 'auth/OTP.html')
        
@never_cache
def UserLogout(request):
    logout(request)
    return redirect('user-login')