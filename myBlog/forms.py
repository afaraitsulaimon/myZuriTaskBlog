from django import forms

from .models import Post, BlogComment




class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = [

            'blogpost_connected',
            'comment_content'
            ]

        widgets = {

            
            'comment_content': forms.Textarea(attrs={'class':'form-control'})
        }



