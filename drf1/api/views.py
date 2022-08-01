from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


def student_detail(request):
    stu = Student.objects.get(id=2)
    serializer = StudentSerializer(stu)
    jason_data = JSONRenderer().render(serializer.data)
    print(jason_data)
    return HttpResponse(jason_data, content_type="aplication/json")
