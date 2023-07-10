from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import *

# Create your views here.

@never_cache
def Home(request):
    if request.user.is_authenticated:
        return redirect('settings')
    else:
        return render(request, "Frontend/home.html")

@never_cache
@login_required(login_url='user-login')
def Chats(request):
    return render(request, 'Frontend/main.html')

@never_cache
@login_required(login_url='user-login')
def Settings(request):
    user = CustomUser.objects.get(username=request.user)
    if request.method == "POST":
        username = request.POST.get('username')
        about = request.POST.get('about')
        if username is not None:
            user.username = username
        if about is not None:
            user.about = about
        user.save()
        return redirect('settings')
    else:
        return render(request, "Frontend/settings.html")
    
@never_cache
@login_required(login_url='user-login')
def Change_pic(request):
    if request.method == "POST":
        user = CustomUser.objects.get(username=request.user)
        pic = request.FILES.get('picture')
        print(pic)
        user.profile_picture = pic
        user.save()
        return redirect('settings')

@never_cache
@login_required(login_url='user-login')
def AddFriends(request):
    users = CustomUser.objects.all().exclude(username=request.user, user_requested__status='requested')
    context = {
        'users': users
    }
    return render(request, 'Frontend/AddFriends.html', context)