from rest_framework.serializers import ModelSerializer

from tournaments.models import Tournament


class TournamentSerializer(ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'
        read_only_fields = ('user',)
