from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


def student_detail(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)
