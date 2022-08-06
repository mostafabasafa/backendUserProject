from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    birthday = models.CharField(max_length=255)
    gender = models.IntegerField()
    province = models.IntegerField()
    city = models.IntegerField()
    activity = models.BooleanField()
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
