# Generated by Django 4.0.3 on 2022-11-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_subsite_notice_subsites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsite',
            name='name',
            field=models.CharField(help_text="This field should match the subdomain name. e.g. for a 'genome.usegalaxy.org' subsite, the name should be 'genome'. This also determines the URL as: '/landing/<subsite.name>'. The HTML template for this landing page must be created manually.", max_length=30, unique=True),
        ),
    ]