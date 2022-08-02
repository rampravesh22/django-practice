from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
import io
# Create your views here.


def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': "Data inserted"
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="aplication/json")


def student_detail(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data, safe=False)
