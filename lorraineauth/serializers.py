from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

   
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

   
    class Meta:
        model = CustomUser
    
        fields = ['email', 'username', 'f_name','l_name','password']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return CustomUser.objects.create_user(**validated_data)

