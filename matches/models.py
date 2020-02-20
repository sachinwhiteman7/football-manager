from django.db import models

from teams.models import Team
from tournaments.models import Group, Tournament

SCHEDULED = "scheduled"
FIRST_HALF = "first half"
HALF_TIME = "half time"
SECOND_HALF = "second half"
EXTRA_FIRST_HALF = "extra first half"
EXTRA_SECOND_HALF = "extra second half"
EXTRA_HALF_TIME = "extra half time"
TIE_BREAKER = "tie breaker"
OVER = "over"
ABANDONED = "abandoned"


MATCH_STATUS_CHOICES = (
    (SCHEDULED, "scheduled"),
    (FIRST_HALF, "first half"),
    (HALF_TIME, "half time"),
    (SECOND_HALF, "second half"),
    (EXTRA_FIRST_HALF, "extra first half"),
    (EXTRA_SECOND_HALF, "extra second half"),
    (EXTRA_HALF_TIME, "extra half time"),
    (TIE_BREAKER, "tie breaker"),
    (OVER, "over"),
    (ABANDONED, "abandoned")
)

HOME_WIN = "home win"
AWAY_WIN = "away win"
DRAW = "draw"

MATCH_RESULT_CHOICES = (
    (HOME_WIN, "home win"),
    (AWAY_WIN, "away win"),
    (DRAW, "draw")
)


class Match(models.Model):
    """
    Model representing a football team.
    """
    tournament = models.ForeignKey(
        Tournament,
        null=True,
        on_delete=models.SET_NULL
    )
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    kickoff = models.DateTimeField(null=True)
    home_team = models.ForeignKey(
        Team,
        null=True,
        on_delete=models.SET_NULL,
        related_name='home_team'
    )
    away_team = models.ForeignKey(
        Team,
        null=True,
        on_delete=models.SET_NULL,
        related_name='away_team'
    )
    status = models.CharField(
        max_length=32,
        choices=MATCH_STATUS_CHOICES,
        default=SCHEDULED
    )
    home_team_goals = models.PositiveSmallIntegerField(default=0)
    away_team_goals = models.PositiveSmallIntegerField(default=0)
    result = models.CharField(
        max_length=32,
        choices=MATCH_RESULT_CHOICES,
        default=DRAW
    )


class MatchPhoto(models.Model):
    description = models.CharField(max_length=1024, default='')
    photo = models.ImageField(upload_to="photos/matches")
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
