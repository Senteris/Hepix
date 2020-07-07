# Generated by Django 3.0.7 on 2020-07-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200706_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='is_sold',
        ),
        migrations.RemoveField(
            model_name='key',
            name='plan',
        ),
        migrations.AddField(
            model_name='key',
            name='duration',
            field=models.IntegerField(default='30', verbose_name='Duration in days'),
        ),
    ]
