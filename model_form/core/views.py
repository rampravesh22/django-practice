from django.shortcuts import render
from core.forms import StudentRegistration
# Create your views here.
def add_student(request):
    if request.method == "POST":
        pass
    
    form = StudentRegistration()
    context={ 
             "form":form
    }
    return render(request,"core/home.html",context)