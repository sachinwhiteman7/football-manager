from django.db import models

from matches.models import Match
from players.models import Player
from teams.models import Team

HEADER = "header"
FREE_KICK = "freekick"
PENALTY = "penalty"
OWN_GOAL = "own goal"
GOAL = "goal"

GOAL_CHOICES = (
    (HEADER, "header"),
    (FREE_KICK, "freekick"),
    (PENALTY, "penalty"),
    (OWN_GOAL, "own goal"),
    (GOAL, "goal")
)


class Goal(models.Model):
    """
    Model for a Goal.
    """
    scored_by = models.ForeignKey(
        Player,
        null=True,
        on_delete=models.SET_NULL,
        related_name="scorer"
    )
    assisted_by = models.ForeignKey(
        Player,
        null=True,
        on_delete=models.SET_NULL,
        related_name='assist'
    )
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    jersey_number = models.PositiveSmallIntegerField(default=0)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    time = models.PositiveSmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now=True)
    goal_type = models.CharField(max_length=32, default=GOAL)
