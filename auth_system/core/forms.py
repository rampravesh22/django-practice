from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django import forms
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput({'class': "form-control"}))
    password2 = forms.CharField(max_length=200, required=True,
                                label="Password Confirmation", widget=forms.PasswordInput({'class': "form-control"}))
    # email = forms.EmailField(required=True,error_messages={"required":"Hello there"})

    class Meta:
        model = User
        # fields = ["username"]
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
        }


class UpdateUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  'email', "date_joined", "email"]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'date_joined': forms.DateTimeInput(attrs={"class": "form-control"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Username", widget=forms.TextInput(
        attrs={"class": "form-control", 'autocomplete': "off"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({
            'class': "form-control",
            'autocomplete': 'current-password'
        })


class ChangeWithOld(PasswordChangeForm):
    old_password = forms.CharField(
        label="Enter old Password", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password1 = forms.CharField(
        label="New Password", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password2 = forms.CharField(
        label="New Password Confirms", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    # old_password = forms.CharField(label="Enter old Password",widget=forms.PasswordInput())


class ChangeWithoutOld(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New Password", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password2 = forms.CharField(
        label="New Password Confirms", widget=forms.PasswordInput(attrs={'class': "form-control"}))
    # old_passwo
