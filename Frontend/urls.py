from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('chats/', Chats, name='chats'),
    path('chats/<int:id>', ShowChat, name='show-chats'),
    path('settings/', Settings, name='settings'),
    path('change-picture/', Change_pic, name='change-picture'),
    path('add-friends/', AddFriends, name='add-friends'),
    path('send-request/<int:id>', SendFriendRequest, name='send-request'),
    path('accept-request/<int:id>', AcceptRequest, name='accept-request'),
    path('cancel-request/<int:id>', CancelRequest, name='cancel-request'),
    path('decline-request/<int:id>', DeclineRequest, name='decline-request'),
    path('mark-as-read/<int:id>', MarkAsRead, name='mark-as-read'),
    path('mark-all', MarkAll, name='mark-all'),
    path('inbox', Inbox, name='inbox'),
]