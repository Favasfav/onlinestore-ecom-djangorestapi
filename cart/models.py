from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=25)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    product_image=models.ImageField( upload_to='products/')
    def __str__(self) -> str:
        return self.product_name
class Cart(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    qty=models.PositiveIntegerField()
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total=models.DecimalField( max_digits=25, decimal_places=2,default=0)
    def create_cart(self,request):
        data=request.data
        print(data)
        return 
    def __str__(self) -> str:
        id=str(self.id)
        return id  
