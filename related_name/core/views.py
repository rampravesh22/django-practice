from django.shortcuts import render
from core.models import Course, Student, Section, Subject
# Create your views here.
print("********************************************************")
print("********************************************************")
print()


subject = Subject.objects.get(id=1)
# print(student.values())
# print(student.course.all().values())
print(subject.student.all())

print()
print("********************************************************")
print("********************************************************")


def home(request):
    return render(request, "core/home.html")
