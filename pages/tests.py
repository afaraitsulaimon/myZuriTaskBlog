from django.test import TestCase
from myBlog.models import Post
from myBlog.models import BlogComment
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(

            username = 'mynewuser',
            email = 'user@aol.com',
            password = 'topuserpw'

        )
        
        self.content = Post.objects.create(

            title = 'A new wa to start',
            author = self.user,
            body = 'What a great way to start coding',
            created_on = ""
            
        )