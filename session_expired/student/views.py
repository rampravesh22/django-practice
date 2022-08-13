from django.shortcuts import render
# Create your views here.
def set_session(request):
    request.session.set_expiry(0) # 0 means when the browser get closed then the session gets expired  
    request.session['name'] = "Rampravesh Chaudhari"
    request.session['age'] = 23
    return render(request, "student/setsession.html")


def get_session(request):
    name=request.session.get('name')
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, "student/getsession.html",{'name':name})

def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, "student/delsession.html")