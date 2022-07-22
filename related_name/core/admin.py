from django.contrib import admin
from core.models import Course, Student, Section, Subject
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'student']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_name', 'student')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name', "all_name")
