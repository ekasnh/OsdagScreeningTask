from rest_framework import viewsets
from .models import RectangularPrism
from .serializers import RectangularPrismSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .prism_calculator import PrismCalculator

class RectangularPrismViewSet(viewsets.ModelViewSet):
    queryset = RectangularPrism.objects.all()
    serializer_class = RectangularPrismSerializer

    @action(detail=True, methods=['get'])
    def calculate(self, request, pk=None):
        prism = self.get_object()
        surface_area = PrismCalculator.calculate_surface_area(prism.length, prism.width, prism.height)
        volume = PrismCalculator.calculate_volume(prism.length, prism.width, prism.height)
        return Response({'surface_area': surface_area, 'volume': volume})
