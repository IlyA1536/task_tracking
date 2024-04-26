# Generated by Django 5.0.3 on 2024-04-26 21:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_comment_media'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='profile_media/')),
                ('name', models.CharField(max_length=63)),
                ('surname', models.CharField(max_length=63)),
                ('description', models.TextField(blank=True)),
                ('birthday_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
