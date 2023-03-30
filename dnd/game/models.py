from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Игра',
        help_text='Создайте игру',
    )
    users = models.ManyToManyField(
        User,
        related_name='games',
    )

    def __str__(self) -> str:
        return self.name
