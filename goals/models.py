from django.db import models

from matches.models import Match
from players.models import Player
from teams.models import Team


class Goal(models.Model):
    """
    Model for a Goal.
    """
    scored_by = models.ForeignKey(Player, on_delete=models.CASCADE)
    assisted_by = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    jersey_number = models.PositiveSmallIntegerField(default=0)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    time = models.PositiveSmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now=True)
    is_own_goal = models.BooleanField(default=False)
