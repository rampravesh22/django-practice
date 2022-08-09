from django import forms
from core.models import Student
from core import choices
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        # custom label name
        labels = {
            "name": "Name Bhare"
        }
        # help text
        help_text = {
            'name': "Please Enter your name",
            "age": "Please enter age",
            "male": "Please Select gender"
        }
        error_messages = {
            "name": {"required": "Name likna jaruri hai"},
            "age":{"required":"Age shoud be greater than 18"}
        }
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "selected":forms.RadioSelect(attrs={"class":"form-radio-input"},choices=choices.SELECTED),
            'subjects':forms.ChoiceField(attrs={},choices=choices.SUBJECTS)
        }
