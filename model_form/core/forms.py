from django import forms
from core.models import Student
from core import choices
class StudentRegistration(forms.ModelForm):
    # we can also define as normal form
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # subjects = forms.CharField(required=False)
    # selected = forms.ChoiceField(required=False)
    class Meta:
        model = Student
        fields =['name','age','gender']
        # fields = "__all__"  # it select all the field to render on teplate
       # exclude=["gender"]    # it remove the mention field from rendering
        
        # custom label name
        labels = {
            "name": "Name Bhare",
           # "selected":"Select Yes or No"
        }
        # help text
        help_text = {
            'name': "Please Enter your name",
            "age": "Please enter age",
           # "male": "Please Select gender"
        }
        
        error_messages = {
            "name": {"required": "Name likna jaruri hai"},
            "age":{"required":"Age shoud be greater than 18"}
        }
        widgets = {
            "name":forms.FileInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
           # "gender":forms.Select(attrs={"class":"form-control"}),
           # "selected":forms.RadioSelect(attrs={"class":"form-check"},choices=choices.SELECTED),
           # 'subjects':forms.CheckboxSelectMultiple(attrs={"class":"form-check"},choices=choices.SUBJECTS)
        }
