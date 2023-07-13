from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from itertools import zip_longest
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
def ShowChat(request, id):
    user = CustomUser.objects.get(username=request.user)
    friend = CustomUser.objects.get(id=id)
    try:
        conv = Conversation.objects.get(user1=user, user2=friend)
        conv2 = Conversation.objects.get(user1=friend, user2=user)
        msg = Message.objects.filter(conv=conv).order_by('id')
        unseen_messages = msg.filter(receiver=user,status=False)
        unseen_messages.update(status=True)
        if request.method == 'POST':
            chat = request.POST.get('chat')
            message = Message.objects.create(
                        content=chat,
                        sender = user,
                        receiver = friend
                      )
            message.conv.add(conv, conv2)
    except:
        msg = []
    context = {
        'msg':msg,
        'frnd': friend
    }
    return render(request, 'Frontend/chat.html', context)

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
    
@login_required(login_url='user-login')
def Change_pic(request):
    if request.method == "POST":
        user = CustomUser.objects.get(username=request.user)
        pic = request.FILES.get('picture')
        user.profile_picture = pic
        user.save()
        return redirect('settings')

@never_cache
@login_required(login_url='user-login')
def AddFriends(request):
    users = CustomUser.objects.exclude(username=request.user)
    friends = Friend.objects.filter(Q(user1=request.user) | Q(user2=request.user))
    for friend in friends:
        users = users.exclude(Q(username=friend.user1.username)|Q(username=friend.user2.username))
    friend_requests = [FriendRequest.objects.filter(user_send=request.user,user_received=user) for user in users]
    data = zip_longest(users, friend_requests)
    context = {
        'data': data,
    }
    return render(request, 'Frontend/AddFriends.html', context)

@login_required(login_url='user-login')
def SendFriendRequest(request, id):
    friend = CustomUser.objects.get(id=id)
    send = FriendRequest.objects.create(
        user_send=request.user,
        user_received=friend
    )
    notification = Notifications.objects.create(
        user=friend,
        sender = request.user,
        content=f"Friend request from #{request.user}"
    )
    return redirect('add-friends')

@login_required(login_url='user-login')
def AcceptRequest(request, id):
    user = CustomUser.objects.get(id=id)
    req = FriendRequest.objects.get(user_send=user, user_received=request.user)
    notification = Notifications.objects.get(user=request.user, sender=user, type="Request")
    friendship = Friend.objects.create(
        user1=user,
        user2=request.user
    )
    req.delete()
    notification.delete()
    return redirect('inbox')

@login_required(login_url='user-login')
def CancelRequest(request, id):
    friend = CustomUser.objects.get(id=id)
    rqst = FriendRequest.objects.get(user_send=request.user, user_received=friend)
    rqst.delete()
    return redirect('add-friends')

@login_required(login_url='user-login')
def DeclineRequest(request, id):
    user = CustomUser.objects.get(id=id)
    rqst = FriendRequest.objects.get(user_send=user, user_received=request.user)
    notification = Notifications.objects.get(user=request.user, sender=user)
    rqst.delete()
    notification.delete()
    return redirect('inbox')

@never_cache
@login_required(login_url='user-login')
def Inbox(request):
    notification = Notifications.objects.filter(user=request.user).order_by('-id')
    context = {
        'notification': notification
    }
    return render(request, 'Frontend/Inbox.html', context)

@never_cache
@login_required(login_url='user-login')
def MarkAsRead(request, id):
    notification = Notifications.objects.get(id=id)
    notification.status = True
    notification.save()
    return redirect('inbox')

@never_cache
@login_required(login_url='user-login')
def MarkAll(request):
    notification = Notifications.objects.filter(user=request.user)
    notification.update(status=True)
    return redirect('inbox')