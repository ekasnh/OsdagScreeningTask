from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RectangularPrismViewSet

router = DefaultRouter()
router.register(r'prisms', RectangularPrismViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
