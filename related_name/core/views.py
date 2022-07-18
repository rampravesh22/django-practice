from django.shortcuts import render
from core.models import Course,Student
# Create your views here.
def home(request):
    print("***********************************************************************************************")
    student = Student.objects.all()[0]
    print(student.sname.upper())
    for course in student.course.all().values():
        print(course.get('cname'))
    # print(Course.objects.all().values())
    print()
    print("***********************************************************************************************")
    
    return render(request,"core/home.html")
    