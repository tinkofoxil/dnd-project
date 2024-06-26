from django.shortcuts import get_object_or_404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.views import APIView

from dnd_profile.models import Profile, CustomUser, Item, Inventory
from game.models import Game, GameUser, GameSession, Invitation
from users.models import Friendship
from .serializer import (
    ProfileSerializer,
    GameSerializer,
    GameSessionSerializer,
    FriendshipSerializer,
    InvitationSerializer,
    InventorySerializer,
    ItemSerializer,
    GameUserSerializer,
    UserSerializer
)
from .permissions import IsOwnerOrReadOnly, ReadOnly


class UserReadViewSet(viewsets.ReadOnlyModelViewSet):
    """Вюсет для пользователя."""

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ReadOnly, )


class UploadAvatarAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ProfileViewSet(viewsets.ModelViewSet):
    """Вьюсет для профиля/анкеты."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'age', 'race', 'class_name']
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyProfilesViewSet(viewsets.ReadOnlyModelViewSet):
    """Вюсет для персонажей пользователя."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Profile.objects.filter(user=user_id)


class MyInvitationViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        user = self.request.user
        return Invitation.objects.filter(recipient=user)


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
    permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['friend'] = self.kwargs.get('user_id')
        return context

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            friend=get_object_or_404(
                CustomUser, id=self.kwargs.get('user_id')
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
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        game = self.get_object()
        game.status = 'started'
        game.save()
        return Response({'status': 'game started'})

    @action(detail=True, methods=['post'])
    def end(self, request, pk=None):
        game = self.get_object()
        game.status = 'finished'
        game.save()
        return Response({'status': 'game ended'})


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = (permissions.IsAuthenticated, )


class GameUserViewSet(viewsets.ModelViewSet):
    queryset = GameUser.objects.all()
    serializer_class = GameUserSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class GameSessionViewSet(viewsets.ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer

    @action(detail=True, methods=['post'])
    def next_round(self, request, pk=None):
        session = self.get_object()
        session.current_round += 1
        session.save()
        return Response({'status': f'Round {session.current_round} started'})

    @action(detail=True, methods=['post'])
    def end_session(self, request, pk=None):
        session = self.get_object()
        session.end_time = timezone.now()
        session.save()
        return Response({'status': 'Session ended'})
