from django.shortcuts import render
from core.forms import Register
# Create your views here.
def register(request):
    form = Register()
    context={
        "form":form
    }
    return render(request,"core/register.html",context)