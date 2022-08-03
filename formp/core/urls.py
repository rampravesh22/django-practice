from django.urls import path
from core import views
urlpatterns = [
    path("",views.register,name="home"),
    path("edit/",views.edit_student, name="edit")
]
