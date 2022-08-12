from django.shortcuts import render

# Create your views here.
def set_cookies(request):
    response = render(request, "student/setcookie.html")
    response.set_cookie("name","Rampravesh")
    return response

def get_cookies(request):
    print()
    return render(request, "student/get_cookie.html")

def del_cookies(request):
    context={}
    return render(request, "student/del_cookie.html", context)
