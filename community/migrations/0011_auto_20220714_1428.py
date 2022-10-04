# Generated by Django 3.2.13 on 2022-07-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_community_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='featured',
        ),
        migrations.AddField(
            model_name='communitypost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]