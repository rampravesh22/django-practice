from django.shortcuts import render, redirect
from core.models import Course, Student, Section, Subject
# Create your views here.
print("********************************************************")
print("********************************************************")
print()


# student = Subject.objects.filter(student__student_name="Jatin")
# print(student.values())


print()
print("********************************************************")
print("********************************************************")


def home(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, "core/home.html", context)


def show(request, id):
    students = Student.objects.all()
    student = Student.objects.get(pk=id)
    context = {
        'students': students,
        'student': student

    }
    return render(request, "core/home.html", context)


def delete(request, id):
    students = Student.objects.all()
    student = Student.objects.get(pk=id)
    s = student.delete()
    context = {
        'students': students,

    }
    return redirect("/")
