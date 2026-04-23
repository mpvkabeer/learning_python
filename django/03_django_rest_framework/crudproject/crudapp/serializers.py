from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['oid', 'fname', 'lname', 'price', 'mail', 'addr']