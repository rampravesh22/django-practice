from django.shortcuts import render,redirect
from core.forms import SignUp
from django.contrib import messages
# from django.contrib.auth import 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages

# Create your views here.
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

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                password = data["password"]
                user = authenticate(username=username,password=password)
                if user:
                    login(request, user)
                    messages.success(request,"You have loged in successfully")
                    return redirect("/profile/")
                    
        else:
            form = AuthenticationForm()
        
        context={
            "form":form
        }
        return render(request, "core/login.html", context)
    return redirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        context={
            'name':request.user
        }
        return render(request, "core/profile.html", context)
    else:
        return redirect("/login/")
def log_out(request):
    logout(request)
    messages.warning(request, "You have logged out successfully")
    return redirect('/')

def change_pass_with_old_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)  # This is for redirecting to the profile page, if we dont use this method then after changeing the password,
                                                         #it will send to the login page and logout from the session
                                                         # because it will create new session so we have to update the session
            return redirect("/profile/")                 
    else:
        form = PasswordChangeForm(user=request.user)
    
    context={
        'form':form
    }
    return render(request, "core/change_password.html", context)
        
    
    