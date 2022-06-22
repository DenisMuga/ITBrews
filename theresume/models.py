from django.db import models

# Create your models here.
class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Certificate(models.Model):
    course_name = models.CharField(max_length=300)
    institute_name =  models.CharField(max_length=300)
    location =  models.CharField(max_length=300)
    enrollment_date =  models.DateTimeField
    completion_date = models.DateTimeField

    def __str__(self):
        return self.course_name  