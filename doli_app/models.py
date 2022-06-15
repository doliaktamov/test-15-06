from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    zagalovok = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

