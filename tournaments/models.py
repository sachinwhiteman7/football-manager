from django.db import models

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

TYPE_CHOICES = (
    (KNOCK_OUT, "Knock Out"),
    (LEAGUE, "League"),
    (LEAGUE_CUM_KNOCK_OUT, "League cum knockout")
)


class Tournament(models.Model):

    name = models.CharField(max_length=256, default="")
    description = models.TextField()
    logo = models.ImageField(upload_to="/tournament/logos/")
    venue = models.CharField(max_length=256, default="")
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    teams = models.ManyToManyField(Team)
    no_of_teams = models.PositiveIntegerField(default=0)
    winner = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)



