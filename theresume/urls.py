from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from theresume import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('theresume/', views.SkillList.as_view()),
    path('theresume/<int:pk>/', views.SkillDetail.as_view()),
    path('api/testimonial/', views.TestimonialList.as_view()),
    path('api/contactprofile/', views.ContactList.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
