from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class votes(models.Model):
    id_content = models.IntegerField(default=-1)
    id_user = models.IntegerField(default=-1)
    up = models.BooleanField(default=False)
    down = models.BooleanField(default=False)

class tip_model(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=15, null=True)
    date = models.DateField(null=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)