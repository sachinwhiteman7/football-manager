from django.db import models

from teams.models import Team


class Match(models.Model):
    """
    Model representing a football team.
    """
    home_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='home_team')
    away_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='away_team')


class MatchPhoto(models.Model):
    description = models.CharField(max_length=1024)
    photo = models.ImageField(upload_to="photos/matches")
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
