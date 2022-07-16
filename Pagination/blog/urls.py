from django.urls import path
from blog import views
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('create/',views.AddBlog.as_view(), name="create")
    
]
