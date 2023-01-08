from django.urls import path,include

# import routers
from rest_framework import routers



from . import views

router = routers.DefaultRouter()
router.register(r'watches', views.WatchViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]