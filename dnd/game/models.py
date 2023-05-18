from django.db import models

from users.models import User


class Game(models.Model):
    """Модель комнаты."""

    name = models.CharField(
        unique=True,
        max_length=150,
        verbose_name='Название комнаты'
    )

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name


class Invitation(models.Model):
    """Модель приглашения в комнату."""

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='invitations_sent',
        verbose_name='Отправитель'
    )
    recipient = models.ForeignKey(
        User,
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
    user = models.ForeignKey(
        User,
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
