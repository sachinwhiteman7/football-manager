from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from accounts.models import User
from accounts.permissions import IsOwnerOrReadOnly
from accounts.serializers import UserCreateSerializer, UserSerializer


class UserSignupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny, )


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def filter_queryset(self, queryset):
        return self.queryset.filter(id=self.request.user.id)
