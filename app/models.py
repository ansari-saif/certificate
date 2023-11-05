from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    unique_code = models.CharField(max_length=20, unique=True, default=None, null=True, blank=True)
    course_name = models.CharField(max_length=255, default="Live Full Stack Open Source Cohort")
    completion_date = models.DateField(default="2023-11-05")
    def __str__(self):
        return self.name