# Generated by Django 4.0.6 on 2022-07-17 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_training_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='race',
            options={'ordering': ['-year']},
        ),
        migrations.AlterField(
            model_name='training',
            name='duration',
            field=models.IntegerField(default=60, validators=[django.core.validators.MaxValueValidator(360), django.core.validators.MinValueValidator(1)], verbose_name='duration - minutes'),
        ),
    ]
