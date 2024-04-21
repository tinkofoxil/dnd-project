from rest_framework import serializers

from dnd_profile.models import Profile, User, Inventory, Item
from game.models import Game, GameUser, Invitation
from users.models import Friendship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "api_user"
        model = User
        fields = ('pk', 'username')


class FriendshipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    friend = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ('pk', 'user', 'friend')

    def validate(self, data):
        user = User.objects.get(id=self.context['request'].user.id)
        friend = User.objects.get(id=self.context['friend'])
        if user == friend:
            raise serializers.ValidationError(
                'Нельзя добавить самого себя в друзья.'
            )
        if Friendship.objects.filter(user=user, friend=friend).exists():
            raise serializers.ValidationError(
                'Пользователь уже есть у Вас в друзьях!'
            )
        return data


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Profile
        fields = (
            "pk", "name", "age",
            "gender", "image", "race",
            "class_name", "level", "charisma",
            "description", "strength", "dexterity",
            "constitution", "intelligence", "wisdom",
            "user", "user_id"

        )

    def validate_age(self, age):
        if age <= 0:
            raise serializers.ValidationError(
                'Возраст должен быть больше нуля'
            )
        return age

    def validate_level(self, level):
        if level < 0:
            raise serializers.ValidationError(
                'Уровень не может быть отрицательным'
            )
        return level


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id',
            'name',
            'status',
            'start_time',
            'finish_time',
            'players'
        )

    def validate_name(self, name):
        if Game.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                'Комната с таким именем уже существует.'
            )


class InvitationSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(
        source='sender.username',
    )
    recipient = serializers.ReadOnlyField(
        source='recipient.username',
    )
    game = serializers.IntegerField(
        source='game.id',
        read_only=True
    )

    class Meta:
        model = Invitation
        fields = (
            'id',
            'sender',
            'recipient',
            'game'
        )

    def validate(self, data):
        sender = User.objects.get(id=self.context['request'].user.id)
        recipient_id = self.context['view'].kwargs['user_id']
        recipient = User.objects.get(id=recipient_id)

        if sender == recipient:
            raise serializers.ValidationError(
                'Нельзя пригласить самого себя!'
            )

        if Invitation.objects.filter(
            sender=sender,
            recipient=recipient
        ).exists():
            raise serializers.ValidationError('Приглашение уже отправлено!')

        return data


class GameUserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    game = serializers.IntegerField(
        source='game.id',
        read_only=True
    )

    class Meta:
        model = GameUser
        fields = '__all__'

    def validate(self, data):
        user = User.objects.get(id=self.context['request'].user.id)
        game_id = self.context['view'].kwargs['game_id']
        game = User.objects.get(id=game_id)

        if GameUser.objects.filter(
            user=user,
            game=game
        ).exists():
            raise serializers.ValidationError(
                'Вы уже присоединились к комнате.'
            )
        return data


class ItemSerializer(serializers.ModelSerializer):
    character = serializers.IntegerField(
        source='character.id',
        read_only=True
    )

    class Meta:
        model = Item
        fields = (
            'name',
            'image',
            'description',
            'character'
        )


class InvetorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'
