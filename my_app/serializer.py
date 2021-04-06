from rest_framework.serializers import ModelSerializer
from .models import SP500

class SP500Serializer(ModelSerializer):
    class Meta:
        model = SP500
        fields = ["symbol","name","momentum"]
