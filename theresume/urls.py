from django.urls import path,include
from theresume import views
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()

router.register('certificate',CertificateViewSet),

urlpatterns = [
    path('api/',include(router.urls))
]