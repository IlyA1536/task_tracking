# Generated by Django 5.0.3 on 2024-04-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_rename_profile_image_userprofile_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_media',
            field=models.FileField(default='img/default_avatar.jpg', upload_to='static/img/'),
        ),
    ]