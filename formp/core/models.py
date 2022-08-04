from django.db import models
from core.choices import SELECT_GENDER
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=SELECT_GENDER,max_length=100)
