from django.shortcuts import render
from rest_framework import generics
from .models import Skill
from .serializers import SkillSerializer

# Create your views here.



class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
