from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, viewsets

from dnd_profile.models import Profile, User
from game.models import Game
from .serializer import ProfileSerializer, GameSerializer
from .permissions import IsOwnerOrReadOnly, ReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    """Вьюсет для профиля/анкеты."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyProfilesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (ReadOnly,)

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Profile.objects.filter(user=user_id)


class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
