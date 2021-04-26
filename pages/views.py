from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from myBlog.forms import NewCommentForm
from myBlog.models import Post
from myBlog.models import BlogComment
from django.contrib.auth import login, logout, authenticate



# Create your views here.

#view for displaying home

def home_view(request):
    postblog = Post.objects.all()
    context = {
        'postblog': postblog
    }
    return render(request, "index.html", context)


#view for diplaying each view you click

def displayBlog_view(request, my_id):

    blogdetails = Post.objects.get(id=my_id)
    
    context = {
        'blogdetailsId': blogdetails
    }


    return render(request, "display-blog-details.html", context)



#view for adding comment to each post

def addComment_view(request, post_id):

    post_details = Post.objects.get(id=post_id)
    formComment = NewCommentForm(request.POST or None)

    if formComment.is_valid():
        formComment.save()
        formComment = NewCommentForm()

    context = {

        "postDetails" : post_details,
        "formCommentTemplate" : formComment
        
    }

    return render(request, 'add_comment.html', context)





#view for registartion

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Acoount Created:{username}")
            form = UserCreationForm()
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')



    form = UserCreationForm

    context = {
        'form' : form
    }
    return render(request, "register.html", context)




#view for login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Inavlid username or password")
        else:
                messages.error(request, "Inavlid username or password")

    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, "login.html", context)
    
   
        


#view for logging out


def logout_view(request):
    logout(request)
    return redirect("login")





