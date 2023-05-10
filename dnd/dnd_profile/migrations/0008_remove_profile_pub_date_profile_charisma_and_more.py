# Generated by Django 4.1.7 on 2023-03-02 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_profile', '0007_dndgame_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='profile',
            name='charisma',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='class_name',
            field=models.CharField(default='asda', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='constitution',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='mda'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='dexterity',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='intelligence',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='race',
            field=models.CharField(default='ork', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='strength',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='wisdom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]