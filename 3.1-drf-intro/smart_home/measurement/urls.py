from django.urls import path

from .views import SensorsView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
