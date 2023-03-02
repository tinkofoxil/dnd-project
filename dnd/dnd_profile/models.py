from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

Genders = [
    ('W', 'Woman'),
    ('M', 'Man'),
    ('N', 'None')
]


class DndGame(models.Model):
    pass


class Profile(models.Model):
    """Модель профиля/анкеты игрока."""

    name = models.TextField(
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
    gender = models.CharField(
        choices=Genders,
        max_length=1,
        default='N'
    )
    race = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    level = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
