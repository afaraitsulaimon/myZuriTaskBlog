from django import forms

from .models import Post, BlogComment
from django.contrib.auth.models import User




class NewCommentForm(forms.ModelForm):
    
    class Meta:
        model = BlogComment
        
        fields = [
             
            'blogpost_connected',
            'user',
            'comment_content'

            ]

        widgets = {
 
            'user': forms.Textarea(attrs={'class':'form-control', 'value':'user.id'}),
            'comment_content': forms.Textarea(attrs={'class':'form-control'}),
            'user': forms.HiddenInput()
        }


class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        
        fields = [
             
            'title',
            'author',
            'content'

            ]

     



