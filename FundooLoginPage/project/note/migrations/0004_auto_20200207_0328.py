# Generated by Django 2.2 on 2020-02-07 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_note_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='date_posted',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_image',
            new_name='image',
        ),
        migrations.AddField(
            model_name='note',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='label',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='label',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Label_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='label',
            field=models.ManyToManyField(blank=True, to='note.Label'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Note_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
