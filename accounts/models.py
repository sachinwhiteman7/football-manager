from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# ADMIN = "admin"
ORGANISER = "organiser"
TEAM_MANAGER = "team manager"
# PLAYER = "player"

ROLE_CHOICES = (
    (ORGANISER, "Organiser"),
    (TEAM_MANAGER, "Team Manager")
)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='photos/profile', blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default=ORGANISER)
