from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from api.category.models import Category
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255, default="This is a description")
    price=models.CharField(max_length=10)
    stock=models.CharField(max_length=10)
    is_active=models.BooleanField(default=True, blank=True)
    image=models.ImageField(upload_to='img/%Y/%m/', blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,  blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name