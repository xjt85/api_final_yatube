# Generated by Django 2.2.16 on 2022-01-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Подписка на пользователя', 'verbose_name_plural': 'Подписки на пользователей'},
        ),
    ]
