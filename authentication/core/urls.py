from django.urls import path
from core import views
urlpatterns=[
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    
]