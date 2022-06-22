from django.shortcuts import render
from .models import Certificate
from rest_framework.viewsets import ModelViewSet
from .serializers import CertificateSerializer

# Create your views here.
class CertificateViewSet(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

# class CertificateViewSet(ModelViewSet):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer    
