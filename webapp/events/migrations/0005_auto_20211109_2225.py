# Generated by Django 3.2 on 2021-11-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20211109_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]