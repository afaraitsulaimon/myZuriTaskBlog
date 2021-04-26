from django.contrib import admin

from .models import UserRegistration, Post, BlogComment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content','created_on')
    list_filter = ("author",)
    search_fields = ['title', 'content']


class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email','password')
    list_filter = ("firstname",)
    search_fields = ['firstname', 'email']

admin.site.register(UserRegistration, UserRegistrationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)

