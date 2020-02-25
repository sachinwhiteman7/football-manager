from rest_framework import viewsets

from accounts.models import User
from accounts.permissions import IsOwnerOrReadOnly
from accounts.serializers import UserCreateSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer

    # permission_classes = (IsOwnerOrReadOnly,)
