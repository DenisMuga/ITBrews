from django.shortcuts import render
from .serializer import MediaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Media

# Create your views here.
class Media(APIView):
    def get(self, request, format=None):
        all_medias = Media.objects.all()
        serializers = MediaSerializer(all_medias, many=True)
        return Response(serializers.data)  