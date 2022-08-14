from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class SignUp(UserCreationForm):
    password2 = forms.CharField(max_length=200, required=True,label="Password Confirmation",widget=forms.PasswordInput())
    # email = forms.EmailField(required=True,error_messages={"required":"Hello there"})
    class Meta:
        model = User
        # fields = ["username"]
        fields = ["username","first_name","last_name","email"]
        
        
class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields=["username","first_name","last_name",'email',"date_joined","email"]
        
class LoginForm(AuthenticationForm):
    # username = forms.CharField(label="Email or Username")
    class Meta:
        model = User
        fields = ["username",'password']
        label = {
            'username':"username/email"
        }
        widgets = {
            "username":forms.TextInput(attrs={'class':"Hello"})
        }