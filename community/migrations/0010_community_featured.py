# Generated by Django 3.2.13 on 2022-07-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_community_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]