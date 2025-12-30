from django.http import HttpResponse

def views(request):
    return HttpResponse('<h1>Home page</h1>')