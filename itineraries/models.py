from django.db import models
from destinations.models import Destination

# Create your models here.


class Itinerary(models.Model):
    destinations = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
