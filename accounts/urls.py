
from django.urls import path,include

from .views import UserSignupAPI,LoginApi
    
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/',UserSignupAPI.as_view()),
     path('login/',LoginApi.as_view()),
]
