from .models import Weather, Weather_Yield,Weather_status
from rest_framework import serializers 

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = "__all__"

class WeatherYieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather_Yield
        fields = "__all__"

class WeatherStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather_status
        fields = "__all__"
    