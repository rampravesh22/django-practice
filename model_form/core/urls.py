from django.urls import path
from core import views
urlpatterns=[
    path("",views.add_student,name="home")
]