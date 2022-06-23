from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TestimonialSerializer, ContactSerializer, SkillSerializer, PortfolioSerializer, BlogSerializer, MediaSerializer
from .models import ContactProfile, Testimonial, Skill, Portfolio, Blog, Media
from rest_framework.parsers import JSONParser 

# Create your views here.

class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class TestimonialList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_testimonials = Testimonial.objects.all()
        serializers = TestimonialSerializer(all_testimonials, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = TestimonialSerializer(data=request.data)
        
class PortfolioList(APIView):
    def get(self, request, format=None):
        all_portfolios = Portfolio.objects.all()
        serializers = PortfolioSerializer(all_portfolios, many=True)
        return Response(serializers.data)  

    def post(self, request, format=None):
        serializers = PortfolioSerializer(data=request.data)
        
class MediaList(APIView):
    def get(self, request, format=None):
        all_medias = Media.objects.all()
        serializers = MediaSerializer(all_medias, many=True)
        return Response(serializers.data)  
    def post(self, request, format=None):
        serializers = MediaSerializer(data=request.data)
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
    
    def delete(self, request, format=None):
        all_portfolios = Portfolio.objects.all().delete()
        return Response({'message': 'Portfolio was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
class BlogList(APIView):
    def get(self, request, format=None):
        all_blogs = Blog.objects.all()
        serializers = BlogSerializer(all_blogs, many=True)
        return Response(serializers.data) 

    def post(self, request, format=None):
        serializers = BlogSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        all_portfolios = Blog.objects.all().delete()
        return Response({'message': 'Blog was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        media_serializer = MediaSerializer(data=request.data) 
        if media_serializer.is_valid(): 
            media_serializer.save() 
            return Response(media_serializer.data) 
        return Response(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, format=None):
        all_medias = Media.objects.all().delete()
        return Response({'message': 'Media was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
