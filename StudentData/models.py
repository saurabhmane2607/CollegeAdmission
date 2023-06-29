from django.db import models

# Create your models here.
class Stud(models.Model):
    student_name = models.CharField (max_length=30)
    class_year = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)