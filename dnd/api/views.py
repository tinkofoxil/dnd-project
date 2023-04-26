from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, viewsets, permissions, status

from dnd_profile.models import Profile, User
from game.models import Game
from users.models import Friendship
from .serializer import ProfileSerializer, GameSerializer, FriendshipSerializer
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


class FriendsListViewSet(viewsets.ModelViewSet):
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class FriendsCreateDestroyViewSet(viewsets.ViewSet):
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, user_id=None):
        friend = User.objects.get(id=user_id)
        Friendship.objects.create(user=request.user, friend=friend)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, user_id=None):
        friend = User.objects.get(id=user_id)
        Friendship.objects.filter(user=request.user, friend=friend).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
