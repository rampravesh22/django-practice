from typing import Optional
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from school.models import Student
# Create your views here.
# ListView Example
class StudentListView(ListView):
    model = Student

# DetailView
class StudentDetailView(DetailView):
    model = Student
    template_name: str = 'school/student.html'    
    
