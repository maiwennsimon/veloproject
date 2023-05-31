from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Bike(models.Model):
    id = models.fields.AutoField(primary_key=True)

    class State(models.TextChoices):
        GOOD = 'G'
        VERY_GOOD = 'VG'
        PERFECT = 'P'
        NEW = 'N'
        BAD = 'B'

    state = models.fields.CharField(choices=State.choices, max_length=5)
    color = models.fields.CharField(max_length=30)
    brand = models.fields.CharField(max_length=100)
    reserved = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'



class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)



class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'