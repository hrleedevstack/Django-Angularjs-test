from .models import Data
from rest_framework import serializers, viewsets

class DataSerializer(serializers.ModelSerializer):

  class Meta:
    model = Data
    fields = '__all__'

class DataVeiwSet(viewsets.ModelViewSet):
  queryset = Data.objects.all()
  serializer_class = DataSerializer