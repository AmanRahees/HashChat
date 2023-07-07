from django.shortcuts import render, redirect

# Create your views here.

def AdminLogin(request):
    return render(request, 'auth/Lock.html')

def Dashboard(request):
    return render(request, "Backend/Dashboard.html")

def UserManagement(request):
    return render(request, 'Backend/ManageUser.html')