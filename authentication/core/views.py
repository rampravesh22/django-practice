from django.shortcuts import render, redirect
# from core.forms import Register
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            pass
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, "core/register.html", context)
