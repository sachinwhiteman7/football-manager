from django.conf.urls import url, include
from rest_framework import routers
from accounts.viewsets import UserSignupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'signup', UserSignupViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]
