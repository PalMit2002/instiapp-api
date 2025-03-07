# Generated by Django 3.2.13 on 2022-07-02 20:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bodies', '0023_body_canonical_name'),
        ('users', '0038_auto_20210606_2237'),
        ('community', '0002_alter_communitypost_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='body',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_body', to='bodies.body'),
        ),
        migrations.AlterField(
            model_name='communitypostuserreaction',
            name='communitypost',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='ucpr', to='community.communitypost'),
        ),
        migrations.AlterField(
            model_name='communitypostuserreaction',
            name='user',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='ucpr', to='users.userprofile'),
        ),
    ]
