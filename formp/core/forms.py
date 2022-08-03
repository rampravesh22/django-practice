from django import forms


class StudentRegister(forms.Form):
    name = forms.CharField(
        required=True, label_suffix=":",widget=forms.TextInput(attrs={"class":"form-control"}))
    age = forms.IntegerField(max_value=100,min_value=18,widget=forms.NumberInput(attrs={"class":"form-control"}))
    gender = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    
