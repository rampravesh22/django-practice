"""login_logout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("register/", views.register, name="register"),
    path('login/',views.user_login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.log_out,name="logout"),
    path('changewith/',views.change_pass_with_old_pass,name="changewith"),
    path('changewithout/',views.change_pass_without_old_pass,name="changewithout"),
    path("updateprofile/", views.update_profile, name="updateprofile"),
    # path("session-expired/", views.session_expired, name="session-expired")
]
