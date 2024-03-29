from django import forms
from django.contrib import admin

from .models import Post, Comment


# How the Post creation form should look
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'author', 'likes', ]


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'author', 'likes_count', 'created_at', 'updated_at', ]
    form = PostAdminForm

    def likes_count(self, obj):
        return obj.likes.count()

    likes_count.short_description = 'Number of likes'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'body', 'likes_count', 'created_at', 'updated_at', ]

    def likes_count(self, obj):
        return obj.likes.count()

    likes_count.short_description = 'Number of likes'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
