# Generated by Django 3.2.13 on 2022-08-22 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0019_remove_communitypost_reported'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitypost',
            name='reported_by',
        ),
    ]
