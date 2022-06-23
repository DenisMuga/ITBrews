from django.contrib.auth import authenticate
from django.forms import ValidationError

from rest_framework import serializers

from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Profile
        fields = ('user', 'prof_pic', 'bio')


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

   
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = CustomUser
    
        fields = ['email', 'username', 'f_name','l_name','profile','password']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        if not email and not password:
            resp = {
                "email": 'Enter a valid email',
                "password": 'Enter a valid password'
                }
            raise serializers.ValidationError(resp)
        LoggedInCustomUser = authenticate(username=email, password=password)
        
        if LoggedInCustomUser is None:
            resp = {
                "error": 'Invalid username or password'
                 }
            raise serializers.ValidationError(resp)
        if not LoggedInCustomUser.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            "email":LoggedInCustomUser.email,
            "username":LoggedInCustomUser.username,
            'token': LoggedInCustomUser.token,
        }