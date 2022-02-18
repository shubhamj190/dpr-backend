from django.contrib import admin
from django.db import models
from .models import Product
from django.utils.html import format_html
# Register your models here.

class ProductSadmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="70"  />'.format(object.image.url))

    list_display =('id','name','myphoto','price','is_active')
    list_display_links=('id','name',)
    list_filter=('category',)
    search_fields=('name',)
    list_editable=('is_active',)

admin.site.register(Product,  ProductSadmin)
