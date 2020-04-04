from django.conf.urls import url, include
from rest_framework import routers
from tournaments.viewsets import TournamentViewSet

router = routers.DefaultRouter()
router.register(r'', TournamentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
