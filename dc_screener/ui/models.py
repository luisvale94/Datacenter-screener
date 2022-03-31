from django.db import models

class datecenter(models.Model):
    name = models.CharField(max_length=200)
    provider_name = models.CharField(max_length=200)
    lng = models.FloatField(max_length=200)
    lat = models.FloatField(max_length=200)


# Create your models here.

