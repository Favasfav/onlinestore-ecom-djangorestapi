
from .models import Cart,Products
from rest_framework import  serializers

# Serializers define the API representation.
class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = '__all__'
        depth=2
    
class Productserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'
       
    
