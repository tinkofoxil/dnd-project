# Generated by Django 4.1.7 on 2024-05-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_profile', '0018_alter_profile_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='charisma_modifier',
            field=models.IntegerField(default=0, verbose_name='Модификатор Харизмы'),
        ),
        migrations.AddField(
            model_name='profile',
            name='constitution_modifier',
            field=models.IntegerField(default=0, verbose_name='Модификатор Телосложения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dexterity_modifier',
            field=models.IntegerField(default=0, verbose_name='Модификатор Ловкости'),
        ),
        migrations.AddField(
            model_name='profile',
            name='intelligence_modifier',
            field=models.IntegerField(default=0, verbose_name='Модификатор Интеллекта'),
        ),
        migrations.AddField(
            model_name='profile',
            name='strength_modifier',
            field=models.IntegerField(default=0, verbose_name='Модификатор Силы'),
        ),
        migrations.AddField(
            model_name='profile',
            name='wisdom_modifier',
            field=models.IntegerField(default=0, verbose_name='Модификатор Мудрости'),
        ),
    ]