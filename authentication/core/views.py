from django.shortcuts import render, redirect
# from core.forms import Register
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    context={}
    return render(request, "core/home.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return redirect("/")
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, "core/register.html", context)
