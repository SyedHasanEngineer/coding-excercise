from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import WeatherSerializer, WeatherYieldSerializer, WeatherStatusSerializer
from .models import Weather, Weather_Yield, Weather_status

class WeatherList(generics.ListAPIView):
    """
    """
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()

class Yield(generics.ListAPIView):
    """
    """
    serializer_class = WeatherYieldSerializer
    queryset = Weather_Yield.objects.all()

class Status(generics.ListAPIView):
    """
    """
    serializer_class = WeatherStatusSerializer
    queryset = Weather_status.objects.all()