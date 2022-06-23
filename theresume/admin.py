from django.contrib import admin
from .models import ContactProfile, Skill, Testimonial,Media,Certificate

admin.site.register(Skill),
admin.site.register(Testimonial),
admin.site.register(ContactProfile),
admin.site.register(Media)
admin.site.register(Certificate)


