from django.contrib import admin
from .models import ContactProfile, Skill, Testimonial
from .models import Skill, Media
from ..lorraineauth.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Skill),
admin.site.register(Testimonial),
admin.site.register(ContactProfile),
admin.site.register(Skill)
admin.site.register(Media)
