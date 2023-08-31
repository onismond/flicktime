import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25, unique=True)
    
    auth_token = models.CharField(max_length=255, null=True)
    auth_type = models.CharField(max_length=10, null=True)
    token_date = models.DateTimeField('date published', default=timezone.now())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password', 'username']

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def token_valid(self):
        now = timezone.now()
        return now - datetime.timedelta(minutes=10) <= self.token_date <= now


