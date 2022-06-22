from rest_framework import serializers
from .models import ContactProfile, Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ( 'name', 'thumbnail', 'role', 'quote', 'is_active')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactProfile
        fields = ( 'timestamp', 'name', 'email', 'message')