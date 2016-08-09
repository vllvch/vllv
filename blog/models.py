from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)