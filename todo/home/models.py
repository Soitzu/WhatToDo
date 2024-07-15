from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.title