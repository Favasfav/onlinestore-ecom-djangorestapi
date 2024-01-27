from django.urls import path, include
from .models import CustomUser
from rest_framework import  serializers

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class Loginserializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()     

