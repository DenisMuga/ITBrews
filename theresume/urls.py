from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from theresume import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()

router.register('certificate',CertificateViewSet),

urlpatterns = [
    path('theresume/', views.SkillList.as_view()),
    path('theresume/<int:pk>/', views.SkillDetail.as_view()),
    path('api/testimonial/', views.TestimonialList.as_view()),
    path('api/contactprofile/', views.ContactList.as_view()),
    path('api/portfolios/', views.PortfolioList.as_view()),
    path('api/blogs/', views.BlogList.as_view()),
    path('api/medias/', views.MediaList.as_view()),
    path('api/',include(router.urls))
    

]

# urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
