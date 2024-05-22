from django.db import models
from users.models import CustomUser
from dnd_profile.models import Profile

GAME_STATUSES = (
    ('created', 'Создана комната'),
    ('started', 'Игра началась'),
    ('finished', 'Игра завершилась')
)


class Game(models.Model):
    """Модель комнаты."""
    name = models.CharField(unique=True, max_length=150, verbose_name='Название комнаты')
    status = models.CharField(max_length=50, choices=GAME_STATUSES, default='created', verbose_name='Статус игры')
    start_time = models.DateTimeField(blank=True, null=True, verbose_name='Время начала игры')
    finish_time = models.DateTimeField(blank=True, null=True, verbose_name='Время завершения игры')
    players = models.ManyToManyField(CustomUser, through='GameUser', verbose_name='Игроки')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name


class Invitation(models.Model):
    """Модель приглашения в комнату."""
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='invitations_sent', verbose_name='Отправитель')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='invitations_received', verbose_name='Получатель')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Комната', related_name='invitations')

    class Meta:
        verbose_name = 'Приглашение в комнату'
        verbose_name_plural = 'Приглашения в комнату'

    def __str__(self):
        return f'{self.sender} --- {self.recipient}'


class GameUser(models.Model):
    """Модель Игрок-Комната."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Игрок')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Комната')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль игрока', related_name='game_users')

    class Meta:
        verbose_name = 'Игра-Пользователь'
        verbose_name_plural = 'Игры-Пользователи'

    def __str__(self):
        return f'{self.user} ({self.profile.name}) --- {self.game}'


class GameSession(models.Model):
    """Модель сессии игры."""
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    current_round = models.IntegerField(default=1, verbose_name='Текущий раунд')
    active_player = models.ForeignKey(GameUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='active_sessions', verbose_name='Активный игрок')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='Время начала сессии')
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='Время завершения сессии')

    class Meta:
        verbose_name = 'Сессия игры'
        verbose_name_plural = 'Сессии игр'

    def __str__(self):
        return f'Сессия игры {self.game.name} - Раунд {self.current_round}'


class PlayerAction(models.Model):
    """Модель для отслеживания действий игрока."""
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, related_name='actions', verbose_name='Сессия игры')
    player = models.ForeignKey(GameUser, on_delete=models.CASCADE, verbose_name='Игрок')
    action_type = models.CharField(max_length=50, verbose_name='Тип действия')
    description = models.TextField(verbose_name='Описание действия')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время действия')

    class Meta:
        verbose_name = 'Действие игрока'
        verbose_name_plural = 'Действия игроков'

    def __str__(self):
        return f'{self.player.user.username} - {self.action_type} - {self.timestamp}'
