from django.db import models
from geopy.geocoders import Nominatim

class Restro(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    pincode = models.CharField(max_length=10)
    lat = models.CharField(max_length=20, null=True, blank=True)
    lon = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="geoapiExercises")
        
        try:
            location = geolocator.geocode(self.pincode)
            if location:
                self.lat = location.latitude
                self.lon = location.longitude
        except Exception as e:
            # Handle geocoding errors, e.g., log the error or set default values
            pass
        
        super(Restro, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
