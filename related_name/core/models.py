from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField()
    
class Course(models.Model):
    cname = models.CharField()