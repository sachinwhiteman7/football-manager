from django.db import models


class Team(models.Model):
    """
    Model to represent a team.
    """
    name = models.CharField(max_length=256, default="")
