# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The username must be set")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def __str__(self):
        return self.username


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
