from typing import Sequence
from django.contrib import admin
from core.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id",'name', 'email', 'age', 'subjects')
    list_editable = ('name', 'email', 'age', 'subjects')
    # list_per_page: int = 2
    search_fields = ("name",)
    # list_filter = ('name',)