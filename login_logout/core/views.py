from django.shortcuts import render,redirect
from core.forms import SignUp
from django.contrib import messages
# from django.contrib.auth import 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
def home(request):
    context={}
    return render(request, "core/home.html", context)

def register(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have signed up successfully")
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        form = SignUp()
    context={
        "form":form
    }
    return render(request, "core/register.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data["password"]
            user = authenticate(username=username,password=password)
            if user:
                login(request, user)
                redirect("profile/")
                
    else:
        form = AuthenticationForm()
    
    context={
        "form":form
    }
    return render(request, "core/login.html", context)

def profile(request):
    context={}
    return render(request, "core/profile.html", context)