from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from school.models import Student
# Create your views here.
# ListView Example
class StudentListView(ListView):
    model = Student

