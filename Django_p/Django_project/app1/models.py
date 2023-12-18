from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
