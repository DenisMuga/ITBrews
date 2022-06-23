from rest_framework import serializers
from theresume.models import ContactProfile, Testimonial, Skill, Portfolio,Blog, Media


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'score', 'image',)
        
        


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ( 'name', 'thumbnail', 'role', 'quote', 'is_active')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactProfile
        fields = ( 'timestamp', 'name', 'email', 'message')

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields='__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields='__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields='__all__'