# Generated by Django 2.2 on 2020-02-17 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0014_auto_20200217_0507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='label',
            new_name='label_note',
        ),
    ]
