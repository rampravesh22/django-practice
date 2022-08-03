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
            Student.objects.create(name=name, age=age, gender=gender)
            
            messages.success(request, "Your data has been saved successfully")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = StudentRegister()
    context={
        'form':form
    }
    return render(request, "core/home.html", context)
