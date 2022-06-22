from django.urls import path
from . import views

urlpatterns=[
   path('api/portfolios/', views.PortfolioList.as_view()),
   path('api/blogs/', views.BlogList.as_view()),

]