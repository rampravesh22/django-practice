from django import forms


class StudentRegister(forms.Form):
    name = forms.CharField(
        required=True, label_suffix="::", initial="Enter your name")
    age = forms.IntegerField()
