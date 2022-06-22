from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import TestimonialSerializer
from .models import ContactProfile, Testimonial
# from .permissions import IsAdminOrReadOnly

# Create your views here.

def index(request):
    return render (request, 'index.html', )

class TestimonialList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_testimonials = Testimonial.objects.all()
        serializers = TestimonialSerializer(all_testimonials, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = TestimonialSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_contacts = ContactProfile.objects.all()
        serializers = ContactSerializer(all_contacts, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ContactSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
