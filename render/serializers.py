from rest_framework.serializers import ModelSerializer

from .models import Watch

class WatchSerializer(ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'