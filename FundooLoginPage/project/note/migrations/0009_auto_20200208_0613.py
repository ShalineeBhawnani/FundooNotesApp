# Generated by Django 2.2 on 2020-02-08 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_auto_20200207_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='add_image',
            new_name='add_picture',
        ),
    ]
