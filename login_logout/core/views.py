from django.shortcuts import render,redirect
from core.forms import SignUp

from django.contrib import messages
# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have signed up successfully")
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        form = UserCreationForm()
    context={
        "form":form
    }
    return render(request, "core/register.html", context)