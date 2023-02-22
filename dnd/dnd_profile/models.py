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
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
