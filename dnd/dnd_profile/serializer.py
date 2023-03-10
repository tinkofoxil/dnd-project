from rest_framework import serializers

from .models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Profile
        fields = (
            "pk", "name", "age",
            "gender", "image", "race",
            "class_name", "level", "charisma",
            "description", "strength", "dexterity",
            "constitution", "intelligence", "wisdom"

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

    def validate_user(self, user):
        if user.is_anonymous:
            raise serializers.ValidationError(
                    'Юзер не может быть анонимным'
                )
        return user
