from django.db import models

from dnd_profile.models import Profile


class Game(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Игра',
        help_text='Создайте игру',
    )
    character = models.ManyToManyField(
        Profile,
        verbose_name='Персонаж',
        related_name='games',
    )

    def __str__(self) -> str:
        return self.name
