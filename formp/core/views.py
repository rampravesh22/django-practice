from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentRegister
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic.list import ListView
# Create your views here.


def home(request):
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
            return redirect('/')
    else:
        form = StudentRegister()
        
        
    students = Student.objects.all()
    
    students = students.order_by("name")
    paginator = Paginator(students,per_page=4,orphans=2)    
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    page_range = paginator.get_elided_page_range(number=page)
    
    context = {
        'form': form,
        'students': students,
        'page_obj':page_obj
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
    student.delete
    student.delete()
    messages.error(
        request, f"{student.name} details is deleted successfully!")
    return redirect("/", kwargs={'student': student})
