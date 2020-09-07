from django.db import models
from itineraries.models import Itinerary

# Create your models here.
class Package(models.Model):
    itineraries = models.ForeignKey(Itinerary, on_delete=models.SET_NULL, null=True)
    description = models.TextField()