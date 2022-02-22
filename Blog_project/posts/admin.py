from django.contrib import admin
from .models import Comment, Post
# Register your models here.
@admin.register(Post)
class Admin_Post (admin.ModelAdmin):
     list_display = ["title", "content", "slug", "author", "created", "modified"]

    

@admin.register(Comment)
class CommentAdmin (admin.ModelAdmin):
    list_display = ["post", "content", "author", "created", "modified"]


