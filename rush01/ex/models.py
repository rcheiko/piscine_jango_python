from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    description = models.CharField(max_length=128)
    profile_picture = models.FileField(upload_to='files')


class Channel(models.Model):
    class Meta:
        unique_together = (('user_id1', 'user_id2'),)

    user_id1 = models.IntegerField()
    user_id2 = models.IntegerField()


class Message(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    value = models.CharField(max_length=128)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.value

class Article(models.Model):
    title = models.CharField(max_length=64, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    content = models.TextField(null=True)

class Commentaire_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=312, null=True)
    created = models.DateTimeField(default=timezone.now)

    def get_child(self):
        return Commentaire_post.objects.filter(comment=self)
