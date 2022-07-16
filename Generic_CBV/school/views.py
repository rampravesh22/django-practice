from ctypes import Union
from typing import Optional
from django import forms
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from school.models import Student
from django.views.generic.edit import CreateView
# Create your views here.
# ListView Example


class StudentListView(ListView):
    model = Student
    template_name: str = 'school/listView/student_list.html'



# DetailView
class StudentDetailView(DetailView):
    model = Student
    template_name: str = 'school/listView/student.html'


class CreateStudentView(CreateView):
    model = Student
    fields = ['name', 'course', 'roll']
    template_name: str = 'school/createView/student_form.html'
    success_url: Optional[str] = '/create/'
    
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':"my-class"})
        return form
