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
    )
    level = models.IntegerField(
        verbose_name='Уровень',
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
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        help_text='Добавьте картинку',
        blank=False,
        null=True,
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    character = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Персонаж'
    )

    class Meta:
        verbose_name = 'Предмет',
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f'{self.name} --- {self.character}'


class Inventory(models.Model):
    character = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Персонаж'
    )
    item = models.ManyToManyField(
        Item,
        verbose_name='Предмет'
    )

    class Meta:
        verbose_name = 'Инвентарь',
        verbose_name_plural = 'Инвентари'

    def __str__(self):
        return f'{self.character} --- {self.item}'
