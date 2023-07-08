from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def AdminLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_superadmin:
                login(request, user)
                return redirect('admin-panel')
            else:
                messages.error(request, "Permission Denied!")
                return redirect('admin-login')
        else:
            messages.error(request, "Invalid Email or Password!")
            return redirect('admin-login')
    else:
        return render(request, 'auth/Lock.html')

@never_cache
def AdminLogout(request):
    logout(request)
    return redirect('admin-login')

@never_cache
@staff_member_required(login_url='admin-login')
def Dashboard(request):
    return render(request, "Backend/Dashboard.html")

def handle_404(request, exception):
    return render(request, '404.html', status=404)

#---------------- UserManagement --------------------------------------------------------------------------------------------

@staff_member_required(login_url='admin-login')
def UserManagement(request):
    return render(request, 'Backend/ManageUser.html')