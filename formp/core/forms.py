from django import forms
from .choices import SELECT_GENDER

class StudentRegister(forms.Form):
    name = forms.CharField(
        initial="", required=True, label_suffix=":", widget=forms.TextInput(attrs={"class": "form-control"}))
    age = forms.IntegerField(max_value=100, min_value=18, widget=forms.NumberInput(
        attrs={"class": "form-control"}))
    gender = forms.ChoiceField(choices=SELECT_GENDER, widget=forms.Select(
        attrs={"class": "form-select w-25"}))
