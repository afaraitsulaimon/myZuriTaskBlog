"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

""" from pages import views
OR do import from your actual view which is below

from pages.views import home_view
what the above means is that from pages.views
(which is from pages folder for one of the app project, look into and get views.py)
then import the function or method called, home_view

then in the path we will change it to 
    path('', home_view, name='home'),

    this is a good convention compare to the first one

"""
from pages.views import home_view, register_view, login_view, displayBlog_view, addComment_view, logout_view, post_view, superuser_login_view, superuser_dashboard_view, admin_logout_view, postupdate_view, postdelete_view

app_name = "pages"

urlpatterns = [

    path('deletepost/<int:id>/delete', postdelete_view, name='deletepost'),
    path('editpost/<int:id>/', postupdate_view, name='editpost'),
    path('adminlogin/', superuser_login_view, name='adminlogin'),
    path('post_new/', post_view, name='post_new'),
    path('logout/',logout_view, name='logout'),
    path('adminlogout/',admin_logout_view , name='adminlogout'),
    path('admin_dashboard/',superuser_dashboard_view , name='admin_dashboard'),
    path('title/<int:post_id>/comment', addComment_view, name='add_comment'),
    path('title/<int:my_id>/', displayBlog_view, name='display-blog-details'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]
