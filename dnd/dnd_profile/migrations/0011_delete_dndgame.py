# Generated by Django 4.1.7 on 2023-04-26 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_profile', '0010_alter_profile_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DndGame',
        ),
    ]