from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.IntegerField(null=True,blank=True,unique=True)
    is_theatre_manager = models.BooleanField(default=False,null=True,blank=True)
    is_approved = models.BooleanField(default=False) 
    otp = models.IntegerField(null=True,blank=True)
    otp_verified = models.BooleanField(default=False)
    otp_expiry = models.DateTimeField(null=True,blank=True)

    '''def __str__(self):
        return self.username  # or return self.email if you prefer''' 