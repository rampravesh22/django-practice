from django import forms


class StudentRegister(forms.Form):
    name = forms.CharField(
        required=True, label_suffix=":",widget=forms.TextInput(attrs={"placeholder":"Enter your name"}))
    age = forms.IntegerField(max_value=100,min_value=18)
    gender = forms.CharField(max_length=100)

    
