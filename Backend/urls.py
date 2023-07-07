from django.urls import path
from .views import *

urlpatterns = [
    path('login/', AdminLogin, name='admin-login'),
    
    path('', Dashboard, name='admin-panel'),

    path('users/', UserManagement, name='manage-users'),
]