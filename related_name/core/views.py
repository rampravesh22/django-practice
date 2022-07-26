from django.shortcuts import render, redirect
from core.models import Course, Student, Section, Subject
from django.contrib import messages
# Create your views here.


# student = Subject.objects.filter(student__student_name="Jatin")
# print(student.values())


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


def addstudnet(request):
    if request.method == "POST":
        print("********************************************************")
        name = request.POST.get('name')
        section = request.POST.get('section')
        courses = request.POST.getlist('course')
        subjects = request.POST.getlist('subjects')
        print(name)
        print(section)
        print(courses)
        print(subjects)
        student = Student.objects.create(student_name=name)

        section = Section.objects.create(student=student, section_name=section)
        for course in courses:
            Course.objects.create(student=student, course_name=course)
        for subject in subjects:
            student.subject.add(
                Subject.objects.create(subject_name=subject))

        messages.success(request, "Student details added successfully")
        print("********************************************************")
        return redirect(request.META.get('HTTP_REFERER'), context={"name": name})

    return render(request, "core/addstudent.html")
