from .models import *
from django.db.models import Q

def NotificationCounter(request):
    try:
        notifications =  Notifications.objects.filter(user=request.user, status=False)
        total = len(notifications)
    except:
        total = 0
    return {'total': total}

def Friends(request):
    try:
        myFriends = Friend.objects.filter(Q(user1=request.user)|Q(user2=request.user))
    except:
        myFriends = []
    return {'myFriends':myFriends}