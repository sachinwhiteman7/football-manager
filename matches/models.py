from django.db import models

from teams.models import Team


class Match(models.Model):

    home_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    away_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)


class MatchPhoto(models.Model):
    description = models.CharField(max_length=1024)
    photo = models.ImageField(upload_to="photos/matches")
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
