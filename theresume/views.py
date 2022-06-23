from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import TestimonialSerializer, ContactSerializer
from .models import ContactProfile, Testimonial
# from .permissions import IsAdminOrReadOnly

# Create your views here

class TestimonialList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    # To get all testimonials
    def get(self, request, format=None):
        all_testimonials = Testimonial.objects.all()
        serializers = TestimonialSerializer(all_testimonials, many=True)
        return Response(serializers.data)
    
    # To get a particular testimonial
    def get_testimonial(self, pk):
        try:
            return Testimonial.objects.get(pk=pk)
        except Testimonial.DoesNotExist:
            return Http404
    
    # To post testimonials
    def post(self, request, format=None):
        serializers = TestimonialSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # To update testimonials
    def put(self, request, format=None):
        serializer = TestimonialSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    # To delete all testimonials
    def delete(self, request, format=None):
        all_testimonials = Testimonial.objects.all().delete()
        return Response({'message': 'Testimonials were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

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
    
