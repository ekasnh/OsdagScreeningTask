from rest_framework import serializers
from .models import RectangularPrism

class RectangularPrismSerializer(serializers.ModelSerializer):
    class Meta:
        model = RectangularPrism
        fields = ['designation', 'length', 'width', 'height']
