# Generated by Django 5.0.3 on 2024-04-27 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_customuser_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='base_user',
        ),
    ]
