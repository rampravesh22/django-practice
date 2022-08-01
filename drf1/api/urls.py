from django.urls import path, include
from api import views
urlpatterns = [
    path("", views.student_detail, name="home")
]
