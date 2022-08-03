from django.urls import path
from core import views
urlpatterns = [
    path("",views.register,name="home"),
    path("edit_student/<int:id>/",views.edit_student, name="edit"),
    path('delete_stduent/<int:id>/',views.delete_student,name="delete")
]
