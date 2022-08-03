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
            return redirect(request.META.get('HTTP_REFERER'))
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
        pass
    else:
        student = Student.objects.get(id=id)
        form = StudentRegister()
    
    context={
        'form':form
    }
    return render(request, "core/edit.html", context)


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.warning(
        request, f"{student.name} details is deleted successfully!")
    return redirect("/", kwargs={'student': student})
