from django.db.models import fields
from rest_framework import serializers
from .models import items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = '__all__'