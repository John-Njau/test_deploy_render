from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    name = "World"
    context = {
        "name": name,
    }
    # return render(request, "hello.html", context)
    return HttpResponse("Hello, World!")