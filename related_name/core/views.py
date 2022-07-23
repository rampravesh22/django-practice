from django.shortcuts import render
from core.models import Course, Student, Section, Subject
# Create your views here.
print("********************************************************")
print("********************************************************")
print()


subject = Subject.objects.get(id=3)
print(subject.student.all().values())

print()
print("********************************************************")
print("********************************************************")


def home(request):
    return render(request, "core/home.html")
