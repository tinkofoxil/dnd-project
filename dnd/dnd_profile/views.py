from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins

from .models import Profile
from .serializer import ProfileSerializer
from .permissions import IsOwnerOrReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    """Вьюсет для профиля/анкеты."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
