from django.contrib import admin
from .models import ContactProfile, Skill, Testimonial
from .models import Skill, Media

# Register your models here.

admin.site.register(Skill),
admin.site.register(Testimonial),
admin.site.register(ContactProfile),
admin.site.register(Skill)
admin.site.register(Media)
