from django.db import models
from django.contrib.auth.models import  User

class Destination(models.Model):
    title=models.CharField(max_length=240)
    pub_date=models.DateField(auto_now_add=False)
    votes_total=models.IntegerField(default=0)
    image=models.ImageField(upload_to="images/")
    icon=models.ImageField(upload_to="icons/")
    body=models.TextField()
    latitude=models.FloatField(blank=True, null=True)
    longitude=models.FloatField(blank=True, null=True)

    # for reference on admin dashboard
    def __str__(self):
        return self.title

    def get_summary(self):
        return self.body[:40] + (self.body[40:] and '..')

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_lat_long(self):
        return f'{self.latitude}, {self.longitude}'

class ImageModel(models.Model):
    mainimage = models.ImageField(upload_to='img', null = True)
    image = models.ForeignKey(Destination, on_delete=models.CASCADE)