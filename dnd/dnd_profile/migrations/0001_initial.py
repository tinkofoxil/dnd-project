# Generated by Django 4.1.7 on 2023-02-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Добавьте имя', max_length=64, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(help_text='Добавьте возраст', verbose_name='Возраст')),
                ('image', models.ImageField(help_text='Добавьте картинку', upload_to='', verbose_name='Картинка')),
            ],
        ),
    ]
