from django.contrib import admin
from .models import ContactProfile, Skill, Testimonial
from .models import Skill, Media
admin.site.register(Skill),
admin.site.register(Testimonial),
admin.site.register(ContactProfile),
admin.site.register(Media)
