from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['-name']),
        ]

    def __str__(self):
        return self.username
