# Generated by Django 4.1.7 on 2023-02-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_profile', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DndGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('W', 'Woman'), ('M', 'Man'), ('N', 'None')], default='N', max_length=1),
        ),
    ]
