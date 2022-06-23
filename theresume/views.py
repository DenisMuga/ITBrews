from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TestimonialSerializer, ContactSerializer, SkillSerializer, PortfolioSerializer, BlogSerializer, MediaSerializer
from .models import ContactProfile, Testimonial, Skill, Portfolio, Blog, Media
from rest_framework.parsers import JSONParser 
from .models import Certificate
from rest_framework.viewsets import ModelViewSet
from .serializers import CertificateSerializer

# Create your views here.

class SkillList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class TestimonialList(APIView):
    permission_classes = (IsAuthenticated,)
    # To get all testimonials
    def get(self, request, format=None):
        all_testimonials = Testimonial.objects.all()
        serializers = TestimonialSerializer(all_testimonials, many=True)
        return Response(serializers.data)
    
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

class TestimonialDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get_Testimonial(self, pk):
        try:
            return Testimonial.objects.get(pk=pk)
        except Testimonial.DoesNotExist:
            return Http404

    # To get a particular testimonial
    def get(self, request, pk, format=None):
        testimonial = self.get_Testimonial(pk)
        serializers = TestimonialSerializer(testimonial)
        return Response(serializers.data)
    
    # To update a particular testimonial
    def put(self, request, pk, format=None):
        testimonial = self.get_Testimonial(pk)
        serializers = TestimonialSerializer(testimonial, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # To get delete a particular testimonial
    def delete(self, request, pk, format=None):
        testimonial = self.get_Testimonial(pk)
        testimonial.delete()
        return Response({'message': 'Testimonial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



class ContactList(APIView):
    permission_classes = (IsAuthenticated,)
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
        
class PortfolioList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        all_portfolios = Portfolio.objects.all()
        serializers = PortfolioSerializer(all_portfolios, many=True)
        return Response(serializers.data)  

    def post(self, request, format=None):
        serializers = PortfolioSerializer(data=request.data)
        
class MediaList(APIView):
    permission_classes = (IsAuthenticated,)
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
    
# class ContactList(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request, format=None):
#         all_contacts = ContactProfile.objects.all()
#         serializers = ContactSerializer(all_contacts, many=True)
#         return Response(serializers.data)
    
#     def post(self, request, format=None):
#         serializers = ContactSerializer(data=request.data)
    
#     def delete(self, request, format=None):
#         all_portfolios = Portfolio.objects.all().delete()
#         return Response({'message': 'Portfolio was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
class BlogList(APIView):
    permission_classes = (IsAuthenticated,)
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


# Create your views here.
class CertificateViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

# class CertificateViewSet(ModelViewSet):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer    
