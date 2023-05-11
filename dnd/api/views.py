from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
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
    """Вюсет для акаунта пользователя."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (ReadOnly,)

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Profile.objects.filter(user=user_id)


class FriendsListViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(user=user)


class FriendsCreateDestroyViewSet(mixins.CreateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    """Вьюсет для добавления/удаления друга."""
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['friend'] = self.kwargs.get('user_id')
        return context

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            friend=get_object_or_404(
                User, id=self.kwargs.get('user_id')
            ))

    @action(methods=['delete'], detail=True)
    def delete(self, request, user_id):
        get_object_or_404(
            Friendship,
            user=request.user,
            friend_id=user_id
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
