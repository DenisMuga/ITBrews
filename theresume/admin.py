from django.contrib import admin
<<<<<<< HEAD
from .models import ContactProfile, Skill, Testimonial

# Register your models here.

admin.site.register(Skill),
admin.site.register(Testimonial),
admin.site.register(ContactProfile),
=======
from .models import Skill, Media

# Register your models here.

admin.site.register(Skill)
admin.site.register(Media)
>>>>>>> 82d6b40363e89a2d8d6dd509c0a4845c400602e1
