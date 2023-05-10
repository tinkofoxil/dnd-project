from rest_framework import serializers

from dnd_profile.models import Profile, User
from game.models import Game
from users.models import Friendship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
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
            "user"

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
            'character'
        )
