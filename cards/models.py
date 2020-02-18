from django.db import models

from matches.models import Match
from players.models import Player
from teams.models import Team


class Card(models.Model):
    """
    Model for a Card.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    time = models.PositiveSmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now=True)


class RedCard(Card):
    """
    Model for red card.
    """
    reason = models.CharField(max_length=256, choices="")


class YellowCard(Card):
    """
    Model for red card.
    """
    reason = models.CharField(max_length=256, choices="")
    is_second_yellow = models.BooleanField(default=False)