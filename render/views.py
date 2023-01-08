from django.shortcuts import render
from django.views import generic

from rest_framework import viewsets

from .models import Watch
from .serializers import WatchSerializer

def index(request):
    watch = "watch"
    return render(request, 'render/index.html', {"context": watch})

class IndexView(generic.ListView):
    queryset = 'watch'
    template_name = 'render/index.html'
    context_object_name = 'watch'


class WatchViewSet(viewsets.ModelViewSet):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer