# Generated by Django 4.0.3 on 2024-01-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_notice_notice_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverimage',
            name='auto_full_width',
            field=models.BooleanField(default=False, help_text="Automatically set the image width to 100% of the screen width. This option overrides 'Max height'."),
        ),
    ]
