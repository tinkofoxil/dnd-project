# Generated by Django 4.1.7 on 2023-02-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_profile', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(help_text='Добавьте картинку', null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]
