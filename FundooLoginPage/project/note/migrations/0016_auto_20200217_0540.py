# Generated by Django 2.2 on 2020-02-17 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0015_auto_20200217_0510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='user',
            new_name='user_id',
        ),
    ]