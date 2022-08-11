from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("This is executed")
        if form.is_valid():
            form.save()
            print("Form.save() executed")
            return redirect("/")
        else:
            return redirect('/')
            print("Form is not valid")
    else:
        form = UserCreationForm()
    context={
        'form':form
    }
    return render(request, "core/home.html", context)