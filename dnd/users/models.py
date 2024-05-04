from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='default_avatar.jpg')
    birth_date = models.DateField(null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)


class Friendship(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='friends'
    )
    friend = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='friended_by',
        verbose_name='Друг'
    )

    class Meta:
        verbose_name = 'Друзья'
        verbose_name_plural = 'Друзья'
        unique_together = ('user', 'friend')

    def __str__(self):
        return f'{self.user.username} - {self.friend.username}'
