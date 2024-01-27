from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.decorators import api_view 
from accounts.serializer import UserSerializer,Loginserializer
from rest_framework import status
from accounts.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class LoginApi(APIView):
    def post(self,request):
        try:
            data=request.data
            print(request.data)
            serializer=Loginserializer(data=data)
            if serializer.is_valid():
                email=serializer.validated_data['email']
                password=serializer.validated_data['password']
                
                user=authenticate(email=email,password=password)
                if user is None:
                    return Response({"data":"invalid"})
                # user=CustomUser.objects.filter(email=email)
                refresh=RefreshToken.for_user(user)
                refresh['username']=user.username
                refresh['email']=user.email
                refresh['phone_no']=user.phone_no
                data={'refresh': str(refresh),
                     'access': str(refresh.access_token),}
                print(refresh)
                return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            pass
    
# Create your views here.
class UserSignupAPI(APIView): 

    def post(self,request):
        print("request.data",request.data)
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user_data = serializer.validated_data
            
                print(user_data,"ser_data")
                user = CustomUser(
                    email =  user_data['email'],
                    phone_no = 'user-' + user_data['phone_no'],
                    username = user_data['username'],
                    password=user_data['password']
                )
                user.set_password(user_data['password'])
                user.save()
                return Response({'message':'Account created successfully.'},status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("mmmmmmmmmmmm",e)
            return Response({
                 
                'message': e,
            }, status=status.HTTP_400_BAD_REQUEST)
    
