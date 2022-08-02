from django.shortcuts import render
from .models import Student
from .forms import StudentRegister
# Create your views here.

def register(request):
    form = StudentRegister()
    context={
        'form':form
    }
    return render(request, "core/home.html", context)
