from django.shortcuts import render

# Create your views here.
def home(request):
    ct = request.session.get("count",0)
    new_count= ct+1
    request.session['count'] = new_count
    context={
        'c':new_count,
    }
    return render(request, "core/home.html", context)
    