# Generated by Django 4.1.7 on 2023-05-18 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0003_remove_game_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.RemoveField(
            model_name='game',
            name='character',
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название комнаты'),
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='game.game', verbose_name='Комната')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Приглашение в комнату',
                'verbose_name_plural': 'Приглашения в комнату',
            },
        ),
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game', verbose_name='Комната')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Игрок')),
            ],
        ),
    ]
