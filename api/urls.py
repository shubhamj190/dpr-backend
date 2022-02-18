
from api.category.models import Category
from django.contrib import admin
from django.urls import path, include
# from rest_framework.authentication import views
from .views import home
from rest_framework.authtoken import views


urlpatterns = [
    path('', home ,name='api.home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
