from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from teams.models import Team

PENDING = "pending"
IN_PROGRESS = "in progress"
COMPLETED = "completed"

STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (IN_PROGRESS, 'In Progress'),
    (COMPLETED, 'completed')
)

KNOCK_OUT = "knock out"
LEAGUE = "league"
LEAGUE_CUM_KNOCK_OUT = "league cum knockout"

TOURNAMENT_TYPE_CHOICES = (
    (KNOCK_OUT, "Knock Out"),
    (LEAGUE, "League"),
    (LEAGUE_CUM_KNOCK_OUT, "League cum knockout")
)

STAGE_TYPE_CHOICES = (
    (KNOCK_OUT, "Knock Out"),
    (LEAGUE, "League")
)


class Tournament(models.Model):

    name = models.CharField(max_length=256, default="")
    description = models.TextField()
    logo = models.ImageField(upload_to="tournament/logos")
    venue = models.CharField(max_length=256, default="")
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    type = models.CharField(max_length=32, choices=TOURNAMENT_TYPE_CHOICES)
    teams = models.ManyToManyField(Team)
    no_of_players_per_team = models.PositiveSmallIntegerField(
        default=11,
        validators=[MaxValueValidator(11)]
    )
    no_of_substitutes_per_team = models.PositiveSmallIntegerField(
        default=0,
        validators=[MaxValueValidator(10)]
    )
    no_of_teams = models.PositiveSmallIntegerField(default=0)
    winner = models.ForeignKey(
        Team,
        null=True,
        on_delete=models.SET_NULL,
        related_name="winner"
    )


class Stage(models.Model):

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default="")
    count = models.PositiveSmallIntegerField(default=0)
    stage_type = models.CharField(max_length=24, choices=STAGE_TYPE_CHOICES, default=KNOCK_OUT)

    class Meta:
        unique_together = ('tournament', 'count')


class Group(models.Model):

    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
    count = models.PositiveSmallIntegerField(default=0)
    number_of_teams = models.PositiveSmallIntegerField(
        default=4,
        validators=[MinValueValidator(2)]
    )

    class Meta:
        unique_together = ('stage', 'count')


class PointsTable(models.Model):

    Group = models.OneToOneField(Group, on_delete=models.CASCADE)


class TeamPointsTable(models.Model):
    points_table = models.ForeignKey(PointsTable, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.PositiveSmallIntegerField(default=0)
    points = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    losses = models.PositiveSmallIntegerField(default=0)
    draws = models.PositiveSmallIntegerField(default=0)
    goal_scored = models.PositiveSmallIntegerField(default=0)
    goal_against = models.PositiveSmallIntegerField(default=0)

    def goal_difference(self):
        return self.goal_scored - self.goal_against
