from django.conf import settings
from django.db import models


class CommonInfo(models.Model):
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Post(CommonInfo):
    title = models.CharField(max_length=50)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    # Use prefetch_related to optimize the query
    # https://docs.djangoproject.com/en/3.1/topics/db/queries/#prefetching-objects

    def __str__(self):
        return self.title


class Comment(CommonInfo):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_likes', blank=True)

    def __str__(self):
        return self.body
