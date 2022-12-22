from django.urls import path
from .views import WeatherList, Yield, Status
urlpatterns = [
    path('weather/', WeatherList.as_view(), name='weather'),
    path("yield/", Yield.as_view(), name='yield'),
    path("weather/stats", Status.as_view(), name='stats')
    ]