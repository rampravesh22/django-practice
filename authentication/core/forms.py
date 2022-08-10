from django.forms import forms,ModelForm
from django.contrib.auth.models import User

class Register(ModelForm):
    class Meta:
        model = User