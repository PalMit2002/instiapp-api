<<<<<<< HEAD
# Generated by Django 3.2.13 on 2022-07-09 11:06
=======
# Generated by Django 3.2.13 on 2022-07-08 12:56
>>>>>>> 10b665612d038145db695783b306c32ebfd1065d

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0012_alter_bodyrole_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyrole',
            name='permissions',
<<<<<<< HEAD
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AddE', 'Add Event'), ('UpdE', 'Update Event'), ('DelE', 'Delete Event'), ('UpdB', 'Update Body'), ('Role', 'Modify Roles'), ('VerA', 'Verify Achievements'), ('ModP', 'Moderate Post'), ('ModC', 'Moderate Comment'), ('DelP', 'Delete Post'), ('DelC', 'Delete Comment')], max_length=49),
=======
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AddE', 'Add Event'), ('UpdE', 'Update Event'), ('DelE', 'Delete Event'), ('UpdB', 'Update Body'), ('Role', 'Modify Roles'), ('VerA', 'Verify Achievements'), ('AddP', 'Add Post'), ('AddC', 'Add Comment'), ('UpdP', 'Update Post'), ('UpdC', 'Update Comment'), ('ModP', 'Moderate Post'), ('ModC', 'Moderate Comment'), ('DelP', 'Delete Post'), ('DelC', 'Delete Comment')], max_length=69),
>>>>>>> 10b665612d038145db695783b306c32ebfd1065d
        ),
    ]
