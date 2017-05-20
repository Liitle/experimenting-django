from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Dashboard</h1> <p>buna rocxica</p>")
