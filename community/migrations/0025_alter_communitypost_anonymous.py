# Generated by Django 3.2.13 on 2022-08-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0024_communitypost_ignored'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='anonymous',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
