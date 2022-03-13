from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    fish = models.CharField(max_length=100, null=True)
    phone_number = models.BigIntegerField(null=True)

# Create your models here.
