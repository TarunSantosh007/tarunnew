# Generated by Django 4.1.1 on 2022-09-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='data',
            field=models.JSONField(default=False),
            preserve_default=False,
        ),
    ]