from django.db import models

from dnd_profile.models import User


class Friendship(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friends'
    )
    friend = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='friended_by',
        verbose_name='Друг'
    )

    class Meta:
        unique_together = ('user', 'friend')

    def __str__(self):
        return f'{self.user.username} - {self.friend.username}'
