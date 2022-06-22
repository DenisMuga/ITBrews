from django.shortcuts import render
from .serializer import PortfolioSerializer, BlogSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Portfolio, Blog
# Create your views here.
class PortfolioList(APIView):
    def get(self, request, format=None):
        all_portfolios = Portfolio.objects.all()
        serializers = PortfolioSerializer(all_portfolios, many=True)
        return Response(serializers.data)  
    
class BlogList(APIView):
    def get(self, request, format=None):
        all_blogs = Blog.objects.all()
        serializers = BlogSerializer(all_blogs, many=True)
        return Response(serializers.data)  