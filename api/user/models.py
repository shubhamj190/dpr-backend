from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    name=models.CharField(max_length=255, default='Anonymous')
    email=models.EmailField(max_length=255, unique=True)
    username=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    gender_choices = (
        ('male','male'),
        ('female','female'),
    )

    phone=models.CharField(max_length=50, blank=True, null=True)
    gender=models.CharField(choices = gender_choices,max_length=10, blank=True, null=True)
    session_token=models.CharField(max_length=10, default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email




