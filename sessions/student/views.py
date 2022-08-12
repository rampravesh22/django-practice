from django.shortcuts import render
# Create your views here.
def set_session(request):
    request.session['name'] = "Rampravesh Chaudhari"
    request.session['age'] = 23
    return render(request, "student/setsession.html")


def get_session(request):
    name=request.session.get('name')
    age=request.session.get('age')
    print(request.session.keys())
    print(request.session.values())
    print(request.session.items())
    return render(request, "student/getsession.html",{'name':name,'age':age})

def del_session(request):
    request.session.flush()
    return render(request, "student/delsession.html")