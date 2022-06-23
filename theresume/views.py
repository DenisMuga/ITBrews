from django.shortcuts import render
from .serializer import PortfolioSerializer, BlogSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Portfolio, Blog
from rest_framework import status

# Create your views here.
class PortfolioList(APIView):
    def get(self, request, format=None):
        all_portfolios = Portfolio.objects.all()
        serializers = PortfolioSerializer(all_portfolios, many=True)
        return Response(serializers.data)  

    def post(self, request, format=None):
        serializers = PortfolioSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
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