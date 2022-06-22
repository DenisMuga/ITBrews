from django.db import models


class Certificate(models.Model):
    course_name = models.CharField(max_length=300)
    institute_name =  models.CharField(max_length=300)
    location = models.CharField(max_length=150)
    
    
    def save_certificate(self):
        self.save()

    def __str__(self):
        return self.course_name

        

          