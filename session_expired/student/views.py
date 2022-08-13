from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_session(request):
    request.session['name'] = "Rampravesh Chaudhari"
    request.session['age'] = 23
    return render(request, "student/setsession.html")


def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name')
        request.session.modified = True
        return render(request, "student/getsession.html",{'name':name})
    else:
        return HttpResponse("<h1 style='color:red;'>Session Has Expired</h1>")
    

def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, "student/delsession.html")