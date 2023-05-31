# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


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

