from django.db import models

from users.models import CustomUser

GAME_STATUSES = (
    ('created', 'Создана комната'),
    ('started', 'Игра началась'),
    ('finished', 'Игра завершилась')
)


class Game(models.Model):
    """Модель комнаты."""

    name = models.CharField(
        unique=True,
        max_length=150,
        verbose_name='Название комнаты'
    )
    status = models.CharField(
        max_length=50,
        choices=GAME_STATUSES,
        default='created',
        verbose_name='Статус игры'
    )
    start_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Время начала игры'
    )
    finish_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Время завершения игры'
    )
    players = models.ManyToManyField(
        CustomUser,
        through='GameUser',
        verbose_name='Игроки'
    )

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name


class Invitation(models.Model):
    """Модель приглашения в комнату."""

    sender = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='invitations_sent',
        verbose_name='Отправитель'
    )
    recipient = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='invitations_received',
        verbose_name='Получатель'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='Комната',
        related_name='invitations'
    )

    class Meta:
        verbose_name = 'Приглашение в комнату'
        verbose_name_plural = 'Приглашения в комнату'

    def __str__(self):
        return f'{self.sender} --- {self.recipient}'


class GameUser(models.Model):
    """Модель Игрок-Комната."""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Игрок'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='Комната'
    )

    class Meta:
        verbose_name = 'Игра-Пользователь'
        verbose_name_plural = 'Игры-Пользователи'

    def __str__(self):
        return f'{self.user} --- {self.game}'
