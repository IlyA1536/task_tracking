# Generated by Django 5.0.3 on 2024-04-26 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_userprofile_default_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_media',
        ),
    ]
