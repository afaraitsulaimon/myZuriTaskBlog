from django import forms

from .models import UserRegistration, Post, BlogComment




class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = [

            'blogpost_connected',
            'comment_content'
            ]



