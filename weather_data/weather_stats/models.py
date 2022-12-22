from django.db import models

# Create your models here.


class Weather(models.Model):
    date = models.DateField(blank=True, null=True, unique=True)
    min_temp = models.CharField(blank=True, null=True, max_length=254)
    max_temp = models.CharField(blank=True, null=True, max_length=254)
    precipitation = models.CharField(blank=True, null=True, max_length=254)

    class Meta:    
        db_table = 'weather'

class Weather_Yield(models.Model):
    date = models.DateField(blank=True, null=True, unique=True)
    corn_gain = models.CharField(blank=True, null=True, max_length=254)

    class Meta:   
        db_table = 'weatheryield'

class Weather_status(models.Model):
    avg_max_temp = models.CharField(blank=True, null=True, unique=True, max_length=254)
    avg_min_temp = models.CharField(blank=True, null=True, max_length=254)
    avg_total_prcecitipation = models.CharField(blank=True, null=True, max_length=254)

    class Meta:   
        db_table = 'weather_status'


