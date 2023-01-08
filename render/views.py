from django.shortcuts import render
from django.views import generic


def index(request):
    watch = "watch"
    return render(request, 'render/index.html', {"context": watch})

class IndexView(generic.ListView):
    queryset = 'watch'
    template_name = 'render/index.html'
    context_object_name = 'watch'


   

