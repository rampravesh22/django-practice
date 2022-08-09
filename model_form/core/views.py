from django.shortcuts import render,redirect
from core.forms import StudentRegistration
# Create your views here.
def add_student(request):
    if request.method == "POST":
        print("Method is POST")
        student_form = StudentRegistration(request.POST)
        
        if student_form.is_valid():
            student_form.save()
            redirect("/")
        
        else:
            print("Not valid")
        
        
    initial_data={
            "name":"Rampravesh",
            "age":21
        }
    form = StudentRegistration(initial=initial_data)
    context={ 
             "form":form
    }
    return render(request,"core/home.html",context)