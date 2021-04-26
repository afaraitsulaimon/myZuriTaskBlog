from django.db import models
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your models here.

class UserRegistration(models.Model):

    firstname = models.CharField(max_length= 32, default='What is your name?')
    lastname = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class BlogComment(models.Model):

    blogpost_connected = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment_content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blogpost_connected.title






    

