from django.shortcuts import render, redirect
from core.forms import SignUp, UpdateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib import messages

# Create your views here.


def home(request):
    context = {}
    if 'session' in request.session:
        request.session.modiefied = True
        return render(request, "core/home.html", context)
    else:
        return redirect("/session-expired/")

def session_expired(request):
    context = {}
    return render(request, "core/session_expired.html", context)

def register(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have signed up successfully")
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        form = SignUp()
    context = {
        "form": form
    }
    return render(request, "core/register.html", context)


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                password = data["password"]
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    request.session['session'] = True
                    messages.success(request, "You have loged in successfully")
                    return redirect("/profile/")

        else:
            form = LoginForm()

        context = {
            "form": form
        }
        return render(request, "core/login.html", context)
    return redirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        context = {
            'name': request.user.first_name
        }
        return render(request, "core/profile.html", context)
    else:
        return redirect("/login/")


def log_out(request):
    logout(request)
    messages.warning(request, "You have logged out successfully")
    return redirect('/')


def change_pass_with_old_pass(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                """ This is for redirecting to the profile page,
					If we dont use this method then after changeing the password,
					it will send to the login page and logout from the session                                                          
                    because it will create new session so we have to update the session """
                return redirect("/profile/")
        else:
            form = PasswordChangeForm(user=request.user)

        context = {
            'form': form
        }
        return render(request, "core/change_pass_with_old_pass.html", context)
    else:
        return redirect('/login/')


def change_pass_without_old_pass(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                """ This is for redirecting to the profile page,
					If we dont use this method then after changeing the password,
					it will send to the login page and logout from the session                                                          
                    because it will create new session so we have to update the session """
                return redirect("/profile/")
        else:
            form = SetPasswordForm(user=request.user)

        context = {
            'form': form
        }
        return render(request, "core/change_pass_with_old_pass.html", context)
    else:
        return redirect('/login/')


def update_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UpdateUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Your profile is updated")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = UpdateUserForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, "core/updateprofile.html", context)
    else:
        return redirect('/login/')


