from django.contrib.auth import get_user_model
from django.db import models

from users.models import CustomUser

class Profile(models.Model):
    """Модель профиля/анкеты игрока."""

    RACE_CHOICES = (
        ('Драконорожденный', 'Dragonborn'),
        ('Дварф', 'Dwarf'),
        ('Эльф', 'Elf'),
        ('Гном', 'Gnome'),
        ('Полуэльф', 'Half-Elf'),
        ('Полуорк', 'Half-Orc'),
        ('Халфлинг', 'Halfling'),
        ('Человек', 'Human'),
        ('Тифлинг', 'Tiefling'),
    )

    CLASS_CHOICES = (
        ('Бард', 'Bard'),
        ('Варвар', 'Barbarian'),
        ('Воин', 'Fighter'),
        ('Волшебник', 'Wizard'),
        ('Друид', 'Druid'),
        ('Жрец', 'Cleric'),
        ('Колдун', 'Warlock'),
        ('Монах', 'Monk'),
        ('Паладин', 'Paladin'),
        ('Плут', 'Rogue'),
        ('Следопыт', 'Ranger'),
        ('Чародей', 'Sorcerer'),
    )

    name = models.CharField(
        max_length=64,
        verbose_name='Имя',
        help_text='Добавьте имя'
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Возраст',
        help_text='Добавьте возраст'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        help_text='Добавьте картинку',
        blank=False,
        null=True,
    )
    race = models.CharField(max_length=50, choices=RACE_CHOICES)
    class_name = models.CharField(
        max_length=50,
        verbose_name='Название класса',
        choices=CLASS_CHOICES
    )
    level = models.IntegerField(
        verbose_name='Уровень',
    )
    proficiency_bonus = models.IntegerField(
        verbose_name='Бонус владения',
        default=2,
    )
    strength = models.IntegerField(
        verbose_name='Сила',
    )
    dexterity = models.IntegerField(
        verbose_name='Ловкость'
    )
    constitution = models.IntegerField(
        verbose_name='Телосложение'
    )
    intelligence = models.IntegerField(
        verbose_name='Интелект'
    )
    wisdom = models.IntegerField(
        verbose_name='Мудрость'
    )
    charisma = models.IntegerField(
        verbose_name='Харизма'
    )
    strength_modifier = models.IntegerField(
        verbose_name='Модификатор Силы', default=0
    )
    dexterity_modifier = models.IntegerField(
        verbose_name='Модификатор Ловкости', default=0
    )
    constitution_modifier = models.IntegerField(
        verbose_name='Модификатор Телосложения', default=0
    )
    intelligence_modifier = models.IntegerField(
        verbose_name='Модификатор Интеллекта', default=0
    )
    wisdom_modifier = models.IntegerField(
        verbose_name='Модификатор Мудрости', default=0
    )
    charisma_modifier = models.IntegerField(
        verbose_name='Модификатор Харизмы', default=0
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='profiles',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(verbose_name='Картинка', help_text='Добавьте картинку', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class Inventory(models.Model):
    character = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Персонаж', related_name='inventory')
    items = models.ManyToManyField(Item, verbose_name='Предметы')

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентари'

    def __str__(self):
        return f'Инвентарь {self.character.name}'
