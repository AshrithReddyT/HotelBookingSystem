from django.db import models
from django.urls import reverse

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=500)

    def __str__(self):
        return self.location_name

class Hotel(models.Model):
    """Model definition for Hotel."""

    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    contact = models.CharField(max_length=100, default='123456789')
    email = models.EmailField(max_length=100, default='hotel_name@email.com')
    amount = models.PositiveIntegerField(default=100)

    def get_absolute_url(self):
        """Return absolute url for Hotel."""
        return reverse('hotel-detail', args=[str(self.pk)])

    def __str__(self):
        """Unicode representation of Hotel."""
        return self.name
