from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='AuthRegistry'),
    path('login/',LoginAPIView.as_view(), name='AuthLogin'),
    path('profile/<str:username>/',ProfileUpdate.as_view(), name='profileupdate'),
  
   
  
]