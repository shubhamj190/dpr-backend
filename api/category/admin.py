from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at','updated_at',)
    list_display_links = ('id','name',)
    list_filter =('name','created_at')
    search_fields =('name',)

admin.site.register(Category, CategoryAdmin)
