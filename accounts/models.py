from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_no']
    phone_no = models.CharField(max_length=30, unique=True, blank=True, null=True)
    def _str_(self): 
        return  self.email 
       