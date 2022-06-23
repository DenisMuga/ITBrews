from django.urls import path
from . import views

urlpatterns=[
   path('api/medias/', views.MediaList.as_view()),
   
]