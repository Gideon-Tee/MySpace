from email.policy import default
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
import uuid
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileImage = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username}'


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'