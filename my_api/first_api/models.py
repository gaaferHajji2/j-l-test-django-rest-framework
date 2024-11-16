from django.db import models

# Create your models here.
class JLCarSpecs(models.Model):
    car_brand           = models.CharField(max_length=50);
    car_model           = models.CharField(max_length=100);
    production_year     = models.CharField(max_length=10);
    car_body            = models.CharField(max_length=100);
    engine_type         = models.CharField(max_length=50);