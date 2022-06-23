from rest_framework import serializers
from .models import ContactProfile, Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ( 'id', 'name', 'thumbnail', 'role', 'quote', 'is_active')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactProfile
        fields = ( 'id', 'timestamp', 'name', 'email', 'message')