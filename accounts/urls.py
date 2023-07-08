from django.urls import path
from .views import *

urlpatterns = [
    path('singup/', UserSingup, name='user-signup'),
    path('login/', UserLogin, name='user-login'),
    path('otp/', otp_verify, name='otp-verify')
]