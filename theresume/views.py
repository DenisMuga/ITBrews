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

    def put(self, request, format=None):
        portfolio_serializer = PortfolioSerializer(data=request.data) 
        if portfolio_serializer.is_valid(): 
            portfolio_serializer.save() 
            return Response(portfolio_serializer.data) 
        return Response(portfolio_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    
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

    def put(self, request, format=None):
        blog_serializer = BlogSerializer(data=request.data) 
        if blog_serializer.is_valid(): 
            blog_serializer.save() 
            return Response(blog_serializer.data) 
        return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, format=None):
        all_portfolios = Blog.objects.all().delete()
        return Response({'message': 'Blog was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
