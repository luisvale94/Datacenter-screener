from django.db import models

class datecenter (models.Model):
    name = models.CharField (max_length=100)
    provider_name = models.CharField (max_length=100)
    lng = models.FloatField (max_length=100)
    lat= models.FloatField (max_length=100)
# Create your models here.
