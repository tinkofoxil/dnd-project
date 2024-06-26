# Generated by Django 4.1.7 on 2024-05-23 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_profile', '0020_profile_proficiency_bonus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Инвентарь', 'verbose_name_plural': 'Инвентари'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='item',
        ),
        migrations.RemoveField(
            model_name='item',
            name='character',
        ),
        migrations.AddField(
            model_name='inventory',
            name='items',
            field=models.ManyToManyField(to='dnd_profile.item', verbose_name='Предметы'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='dnd_profile.profile', verbose_name='Персонаж'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте картинку', null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]
