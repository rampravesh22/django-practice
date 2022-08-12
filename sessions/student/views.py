from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def set_session(request):
    request.session['name'] = "Rampravesh Chaudhari"
    return render(request, "student/setsession.html")


def get_session(request):
    name=request.session['name']
    return render(request, "student/getsession.html",{'name':name})

def del_session(request):
    if 'name' in request.session:
        del request.session['name'] 
    return render(request, "student/delsession.html")