from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('chats/', Chats, name='chats'),
    path('settings/', Settings, name='settings'),
    path('change-picture/', Change_pic, name='change-picture'),
]