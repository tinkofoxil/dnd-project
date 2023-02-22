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

    def validate_user(self, user):
        if user.is_anonymous:
            raise serializers.ValidationError(
                    'Юзер не может быть анонимным'
                )


class ProfileShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("pk", "name", "age", "image")
