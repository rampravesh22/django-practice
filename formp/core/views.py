from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentRegister
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        form = StudentRegister(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            age = data['age']
            gender = data['gender']
            s = Student.objects.create(name=name, age=age, gender=gender)

            messages.success(
                request, f"{s.name} data has been saved successfully")
            return JsonResponse({"Yes":"Suceeded"})
    else:
        form = StudentRegister()
    students = Student.objects.all()
    context = {
        'form': form,
        'students': students
    }
    return render(request, "core/home.html", context)


def edit_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(id=id)
        form = StudentRegister(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            student = Student(id=id)
            student.name=data['name']
            student.age = data['age']
            student.gender = data['gender']
            student.save()
            messages.success(request, "Your data has been updated successfully!")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        student = Student.objects.get(id=id)
        name = student.name
        age = student.age
        gender = student.gender
        form = StudentRegister(initial={"name": name,'age':age,'gender':gender})
    context = {
        'form': form
    }
    return render(request, "core/edit.html", context)


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.error(
        request, f"{student.name} details is deleted successfully!")
    return redirect("/", kwargs={'student': student})
