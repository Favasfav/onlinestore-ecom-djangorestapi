
from django.urls import path,include

from .views import AddtoCartAPI,GetCartlist,GetproductAPI
    
urlpatterns = [
   path('product/',GetproductAPI.as_view(),name='cartlist'),
    path('addtocart/<int:product_id>/<int:qty>/<int:user_id>/',AddtoCartAPI.as_view(),name='addtocart'),
    path('cartlist/<int:user_id>/',GetCartlist.as_view(),name='cartlist'),
   
]