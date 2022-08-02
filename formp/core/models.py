from django.db import models

# Create your models here.


class Student(models.Model):
    gender_choice = (
        ("Male", 'Male'),
        ("Female", "Female"),
        ("Other", "Other")
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=gender_choice, max_length=20)
