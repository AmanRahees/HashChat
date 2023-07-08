from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

# Create your views here.

@never_cache
def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return render(request, "Frontend/home.html")

@never_cache
@login_required(login_url='user-login')
def Profile(request):
    return render(request, "Frontend/main.html")