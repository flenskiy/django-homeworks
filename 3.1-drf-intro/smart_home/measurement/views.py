from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementCreateSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer
