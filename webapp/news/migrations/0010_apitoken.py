# Generated by Django 3.2 on 2021-11-22 03:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_news_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='A name for this token.', max_length=100)),
            ],
        ),
    ]