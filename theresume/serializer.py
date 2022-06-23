from rest_framework import serializers
from .models import Media

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields='__all__'