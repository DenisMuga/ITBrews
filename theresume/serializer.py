from rest_framework import serializers
from .models import Portfolio,Blog

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields='__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields='__all__'