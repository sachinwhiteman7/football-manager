from rest_framework import viewsets

from tournaments.models import Tournament
from tournaments.permissions import IsOwnerOrReadOnly
from tournaments.serializers import TournamentSerializer


class TournamentViewSet(viewsets.ModelViewSet):

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
