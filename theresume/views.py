from django.shortcuts import render
from .models import Certificate
from rest_framework import models
from .serializers import CertificateSerializer

# Create your views here.
class CertificateList(ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CertificateDetail(RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer    
