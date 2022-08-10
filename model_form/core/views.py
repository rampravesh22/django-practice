from django.shortcuts import render,redirect
from core.forms import StudentRegistration
from django.http import JsonResponse
# Create your views here.
def add_student(request):
    if request.method == "POST":
        print("Method is POST")
        student_form = StudentRegistration(request.POST)
        redirect("/")        
    initial_data={
            "name":"Rampravesh",
            "age":21,
            "gender":"Male",
            "subjects":["Math","Hindi","Science"]
        }
    form = StudentRegistration(initial=initial_data)
    context={ 
             "form":form
    }
    return render(request,"core/home.html",context)