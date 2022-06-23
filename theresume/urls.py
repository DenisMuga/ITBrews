from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from theresume import views

urlpatterns = [
    path('theresume/', views.SkillList.as_view()),
    path('theresume/<int:pk>/', views.SkillDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)