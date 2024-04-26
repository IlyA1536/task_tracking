from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To do"),
        ("in_progress", "In progress"),
        ("done", "Done")
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ]

    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=31, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=31, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateTimeField(blank=True, null=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authors")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    media = models.FileField(upload_to="comment_media/",blank=True, null=True)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    name = models.CharField(max_length=63)
    surname = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    birthday_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    default_media = models.FileField(upload_to='static/img/', default='img/default_avatar.jpg')
    media = models.FileField(upload_to='profile_media/', null=True, blank=True)
