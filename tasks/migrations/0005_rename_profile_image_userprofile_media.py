# Generated by Django 5.0.3 on 2024-04-26 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_image',
            new_name='media',
        ),
    ]