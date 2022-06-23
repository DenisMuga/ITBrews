from .backends import JWTAuthentication
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .renderers import UserJSONRenderer
from rest_framework.generics import GenericAPIView
from .models import Profile
from rest_framework.authtoken.models import Token
from .authentication_handlers import *
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


# Create your views here.
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer
    
    def post(self, request):
       
        data = request.data
        user = request.data.get('CustomUser', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        # token = AuthTokenHandler.create_auth_token(user)
        # data["token"] = token.key
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('CustomUser', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProfileUpdate(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    authentication_classes = (JWTAuthentication,) 
     
    def  patch(self, request, username):
        
        try:
            profile = Profile.objects.get(user__username=username)
        except Exception:
            return Response({
            'errors': {
                'user': ['User does not exist']
            }
        }, status=status.HTTP_404_NOT_FOUND)
            
        user_name = request.user.username
        print(user_name)
        if user_name != username:
            return Response({
            'errors': {
                'user': ['You do not own this profile']
            }}, status=status.HTTP_403_FORBIDDEN)

        data = request.data

        serializer = ProfileSerializer(
            instance=request.user.profile,
            data=data,
            partial=True
        )
        serializer.is_valid()
        serializer.save()
        return Response(
            {'profile': serializer.data},
            status=status.HTTP_200_OK
        )
        
    def get(self, request, username):
        """
        Endpoint for fetching user data from Profile model
        """
        try:
            profile = Profile.objects.get(user__username=username)
        except Exception:
            return Response({
                'errors': {
                    'user': ['User does not exist']
                }
            }, status=status.HTTP_404_NOT_FOUND)
       
      
        if profile:
            serializer = ProfileSerializer(
                profile, context={'request': request},
                
            )
           
       
        return Response({
            'profile': serializer.data
        }, status=status.HTTP_200_OK)