from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Register your models here.
class CustomUser(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
