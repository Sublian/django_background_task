from django.db import models
from django.contrib.auth.models import User


class MessageBoard(models.Model):
    subscribers = models.ManyToManyField(User, related_name="messageboards", blank=True)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    messageboard = models.ForeignKey(
        MessageBoard, related_name="messages", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.author.username
