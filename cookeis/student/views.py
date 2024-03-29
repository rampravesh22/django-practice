from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def set_cookies(request):
    response = render(request, "student/setcookie.html")
    response.set_cookie("name","rahul",expires=datetime.utcnow()+timedelta(days=2))
    return response

def get_cookies(request):
    name = request.COOKIES.get("name","This name is not set yet")
    return render(request, "student/getcookie.html",{'name':name})

def del_cookies(request):
    response = render(request, "student/delcookie.html")
    response.delete_cookie('name')
    return response