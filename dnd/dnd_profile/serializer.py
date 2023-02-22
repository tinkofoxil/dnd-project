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
        fields = ("pk", "name", "age", "image",)

    def validate_age(self, age):
        if type(age) is not int:
            raise serializers.ValidationError(
                'Возраст должен быть целочисленным'
            )
        elif age <= 0:
            raise serializers.ValidationError(
                'Возраст должен быть больше нуля'
            )

    def validate_user(self, user):
        if user.is_anonymous:
            raise serializers.ValidationError(
                    'Юзер не может быть анонимным'
                )
