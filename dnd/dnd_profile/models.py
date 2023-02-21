from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
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
        help_text='Добавьте картинку'
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
