# Generated by Django 2.2 on 2020-02-17 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0016_auto_20200217_0540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='user_id',
            new_name='user',
        ),
    ]
