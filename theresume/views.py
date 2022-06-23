from django.shortcuts import render
from .serializer import MediaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Media
from rest_framework import status

# Create your views here.
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

    def put(self, request, format=None):
        media_serializer = MediaSerializer(data=request.data) 
        if media_serializer.is_valid(): 
            media_serializer.save() 
            return Response(media_serializer.data) 
        return Response(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, format=None):
        all_medias = Media.objects.all().delete()
        return Response({'message': 'Media was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
