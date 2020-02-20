from django.db import models


class Venue(models.Model):
    """
    Model to represent a venue.
    """
    name = models.CharField(max_length=256, default="")
    logo = models.ImageField(null=True, blank=True, upload_to="team/logos")
    address_line_1 = models.CharField(max_length=256, default="")
    address_line_2 = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=128, default="")


class VenuePhoto(models.Model):
    """
    Model to represent a Venue photo.
    """
    photo = models.ImageField(upload_to='photos/venue', blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
