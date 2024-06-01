from rest_framework import serializers

from dnd_profile.models import Profile, CustomUser, Inventory, Item
from game.models import Game, GameUser, Invitation, GameSession
from users.models import Friendship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "api_user"
        model = CustomUser
        fields = ('pk', 'username', 'avatar', 'email', 'birth_date', 'registration_date')


class FriendshipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    friend = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ('pk', 'user', 'friend')

    def validate(self, data):
        user = CustomUser.objects.get(id=self.context['request'].user.id)
        friend = CustomUser.objects.get(id=self.context['friend'])
        if user == friend:
            raise serializers.ValidationError(
                'Нельзя добавить самого себя в друзья.'
            )
        if Friendship.objects.filter(user=user, friend=friend).exists():
            raise serializers.ValidationError(
                'Пользователь уже есть у Вас в друзьях!'
            )
        return data



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'image', 'description']


class InventorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'character', 'items']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    inventory = InventorySerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            "pk",
            "name",
            "age",
            "image",
            "race",
            "class_name",
            "level",
            "proficiency_bonus",
            "alignment",
            "background",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
            "strength_modifier",
            "dexterity_modifier",
            "constitution_modifier",
            "intelligence_modifier",
            "wisdom_modifier",
            "charisma_modifier",
            "armor_class",
            "initiative",
            "speed",
            "hit_points",
            "current_hit_points",
            "temporary_hit_points",
            "saving_throws",
            "skills",
            "equipment",
            "traits",
            "ideals",
            "bonds",
            "flaws",
            "description",
            "backstory",
            "user",
            "user_id",
            "inventory",
            "created_at",
            "updated_at",
        )

    def validate_age(self, age):
        if age <= 0:
            raise serializers.ValidationError('Возраст должен быть больше нуля')
        return age

    def validate_level(self, level):
        if level < 0:
            raise serializers.ValidationError('Уровень не может быть отрицательным')
        return level

    def create(self, validated_data):
        validated_data = self.calculate_attributes(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self.calculate_attributes(validated_data, instance)
        return super().update(instance, validated_data)

    def calculate_attributes(self, validated_data, instance=None):
        strength = validated_data.get('strength', instance.strength if instance else None)
        dexterity = validated_data.get('dexterity', instance.dexterity if instance else None)
        constitution = validated_data.get('constitution', instance.constitution if instance else None)
        intelligence = validated_data.get('intelligence', instance.intelligence if instance else None)
        wisdom = validated_data.get('wisdom', instance.wisdom if instance else None)
        charisma = validated_data.get('charisma', instance.charisma if instance else None)
        level = validated_data.get('level', instance.level if instance else None)

        # Calculate modifiers
        validated_data['strength_modifier'] = self.get_ability_modifier(strength)
        validated_data['dexterity_modifier'] = self.get_ability_modifier(dexterity)
        validated_data['constitution_modifier'] = self.get_ability_modifier(constitution)
        validated_data['intelligence_modifier'] = self.get_ability_modifier(intelligence)
        validated_data['wisdom_modifier'] = self.get_ability_modifier(wisdom)
        validated_data['charisma_modifier'] = self.get_ability_modifier(charisma)

        # Calculate proficiency bonus
        validated_data['proficiency_bonus'] = self.get_proficiency_bonus(level)

        # Calculate armor class (example: 10 + dexterity modifier)
        validated_data['armor_class'] = 10 + validated_data['dexterity_modifier']

        # Calculate initiative (dexterity modifier)
        validated_data['initiative'] = validated_data['dexterity_modifier']

        # Calculate speed (default to 30, could be adjusted based on race or class)
        validated_data['speed'] = 30

        # Calculate hit points (example: level * (constitution modifier + 10))
        validated_data['hit_points'] = level * (10 + validated_data['constitution_modifier'])
        validated_data['current_hit_points'] = validated_data['hit_points']
        validated_data['temporary_hit_points'] = 0

        # Initialize saving throws and skills as empty or with default values
        validated_data['saving_throws'] = {}
        validated_data['skills'] = {}

        return validated_data

    def get_ability_modifier(self, ability_score):
        if ability_score is not None:
            return (ability_score - 10) // 2
        return 0

    def get_proficiency_bonus(self, level):
        if level < 5:
            return 2
        elif level < 9:
            return 3
        elif level < 13:
            return 4
        elif level < 17:
            return 5
        else:
            return 6


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['pk', 'name', 'status', 'start_time', 'finish_time', 'players']

    def validate_name(self, name):
        if Game.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                'Комната с таким именем уже существует.'
            )
        return name


class InvitationSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    recipient = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Invitation
        fields = '__all__'

    def create(self, validated_data):
        sender = self.context['request'].user

        validated_data['sender'] = sender

        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sender'] = UserSerializer(instance.sender).data
        representation['game'] = GameSerializer(instance.game).data
        representation['recipient'] = UserSerializer(instance.recipient).data
        return representation


class GameUserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = GameUser
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user

        validated_data['user'] = user

        return super().create(validated_data)

    def validate(self, data):
        user = self.context['request'].user

        profile = data['profile']

        if profile.user != user:
            raise serializers.ValidationError("Этот персонаж не принадлежит вам.")

        return data


class GameSessionSerializer(serializers.ModelSerializer):
    game = serializers.StringRelatedField()
    active_player = serializers.StringRelatedField()

    class Meta:
        model = GameSession
        fields = '__all__'
