from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from myBlog.forms import NewCommentForm, NewPostForm
from myBlog.models import Post
from myBlog.models import BlogComment
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count


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
@login_required
def addComment_view(request, post_id):    
    post_details = Post.objects.get(id=post_id)
    user = User.objects.get(pk=request.user.pk)
    
    if request.method == 'POST':
        formComment = NewCommentForm(request.POST or None)
        if formComment.is_valid():
            formComment.instance.user = request.user
            
            formComment.save()
            formComment = NewCommentForm()

    formComment = NewCommentForm()

    context = {
        
        "user": user,
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



    #view for super login user

def superuser_login_view(request):
    if request.method == "POST":
        form_super_user = AuthenticationForm(request, data = request.POST)
        if form_super_user.is_valid():
                username = form_super_user.cleaned_data.get('username')
                password = form_super_user.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                is_superuser = user.is_superuser
                

                if is_superuser:
                    login(request, user)
                    return redirect("admin_dashboard")
                else:
                    messages.error(request, "Inavlid username or password")
        else:
                messages.error(request, "Inavlid username or password")

    form_super_user = AuthenticationForm()
    context = {

        'form_super_user' : form_super_user
    }
    return render(request, "adminlogin.html", context)
    
   

# view for admin dashboard,
#so that the admin can be
@login_required
def superuser_dashboard_view(request):
    numberOfPost = Post.objects.all()
    numberOfUser = User.objects.all()
    theTotalPost = numberOfPost.count()
    theTotalUser = numberOfUser.count()
 
    adminDetailsForPosts = Post.objects.all()

    context = {

        'theTotalPost' : theTotalPost,
        'theTotalUser' : theTotalUser,
        'adminDetailsForPosts' : adminDetailsForPosts
    }
   
    return render(request, "admin_dashboard.html", context)




#view for posting new
@login_required
def post_view(request):
    if request.method == 'POST':
        formPost = NewPostForm(request.POST or None)
        if formPost.is_valid():
            formPost.save()
    
    formPost = NewPostForm()
    context = {

    'formPost' : formPost
    }

    return render(request, 'post_new.html', context)


    #view for admin to edit post

@login_required
def postupdate_view(request, id):

    object = Post.objects.get(id=id)
    formPost = NewPostForm(request.POST or None,instance=object)

    if request.method == "POST":
        if formPost.is_valid():
             formPost.save()

    return render(request, 'editpost.html', {'formPost':formPost})



# delete view
@login_required
def postdelete_view(request, id):

    obj = get_object_or_404(Post, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('admin_dashboard')   
    
    context = {
        'object' : obj
    }

    return render(request, 'deletepost.html', context)




   

#view for logging out


def logout_view(request):
    logout(request)
    return redirect("login")


#view for admin logout

def admin_logout_view(request):
    logout(request)
    return redirect("adminlogin")





