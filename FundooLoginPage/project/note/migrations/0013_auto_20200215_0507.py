# Generated by Django 2.2 on 2020-02-15 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0012_label_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='user_id',
            new_name='user',
        ),
    ]
