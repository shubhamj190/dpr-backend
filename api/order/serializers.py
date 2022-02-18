from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Order
        fields = ('user','product', )
        # TODO :add product and quantity