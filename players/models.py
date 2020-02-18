from django.db import models

from teams.models import Team


class Player(models.Model):
    """
    Model for a player.
    """
    name = models.CharField(max_length=256, default="")
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    jersey_number = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(upload_to="photos/players")
