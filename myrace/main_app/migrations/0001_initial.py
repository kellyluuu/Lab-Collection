# Generated by Django 4.0.6 on 2022-07-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_name', models.CharField(max_length=100)),
                ('year', models.IntegerField(verbose_name=False)),
                ('race_type', models.CharField(max_length=100)),
                ('distance', models.IntegerField()),
                ('image', models.URLField()),
            ],
        ),
    ]