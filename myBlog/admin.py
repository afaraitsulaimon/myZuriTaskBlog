from django.contrib import admin

from .models import  Post, BlogComment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content','created_on')
    list_filter = ("author",)
    search_fields = ['title', 'content']




admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)

