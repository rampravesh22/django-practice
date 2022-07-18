from django.db import models

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.sname


class Course(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE,related_name="course")
    cname = models.CharField(max_length=100, default="")

