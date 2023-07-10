from django.db import models
from accounts.models import CustomUser

# Create your models here.


class FriendRequest(models.Model):
    user_send = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_requested')
    user_received = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recieved_user')
    status = models.CharField(max_length=50, default='requested')

    def __str__(self):
        return f"Friend Request from {self.user_send} to {self.user_received}"
    
class Friend(models.Model):
    frnd_req = models.ForeignKey(FriendRequest, on_delete=models.CASCADE)
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='frnd_1')
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='frnd_2')

    def __str__(self):
        return f"{self.user1} ---------- {self.user2}"

class Conversation(models.Model):
    name = models.CharField(max_length=100)
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_1')
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_2')

    def __str__(self):
        return f"{self.user1} -----> {self.user2}"
    
class Message(models.Model):
    content = models.CharField(max_length=1024, default='Hello')
    conv = models.ManyToManyField(Conversation)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} -----> {self.receiver}"