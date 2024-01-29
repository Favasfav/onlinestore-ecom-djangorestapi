from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializer import CartSerializer,Productserializer
from rest_framework import status
from accounts.models import CustomUser
from .models import Cart, Products

class GetproductAPI(APIView):
    def get(self,request):
        try:
            product=Products.objects.all()
            print("jjjjjj",product)
            serializer=Productserializer(instance=product,many=True)
            if serializer.data:
                return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddtoCartAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            product_id = self.kwargs.get("product_id")
            qty = self.kwargs.get("qty")
            user_id = self.kwargs.get("user_id")
            user = CustomUser.objects.get(id=user_id)
            product = Products.objects.get(id=product_id)
            stock = product.stock
            if qty > stock and (stock - qty) <= 0:
                return Response(
                    {"message": "no stock"}, status=status.HTTP_400_BAD_REQUEST
                )

            data = {"user": user_id, "product": product_id, "qty": qty}
            serializer = CartSerializer(data=data)
            if serializer.is_valid():
                total=product.price*qty
                Cart(user=user, qty=qty, product=product,total=total).save()
                stock -= qty
                product.stock = stock
                product.save()
                return Response(status=status.HTTP_201_CREATED)

            print(serializer.errors)
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(e)
            return Response(
                {"message": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetCartlist(APIView):
    def get(self,request,*args, **kwargs):
        user_id=self.kwargs.get('user_id')
        try:
            cart_list=Cart.objects.filter(user=user_id)
            print("jjjjjj",cart_list)
            serializer=CartSerializer(instance=cart_list,many=True)
            if serializer.data:
                return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)