from django.db import models
from core import choices
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20,help_text="Enter your full name here", error_messages={})
    age = models.IntegerField()
    gender = models.CharField(choices=choices.GENDER, max_length=20)
    subjects=models.CharField(choices=choices.SUBJECTS,max_length=20,default="Hello")