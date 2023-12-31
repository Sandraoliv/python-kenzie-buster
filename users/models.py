from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)
    is_employee = models.BooleanField(blank=True, null=True, default=False)
   
