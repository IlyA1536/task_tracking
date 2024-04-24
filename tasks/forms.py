from django import forms
from tasks.models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "All"),
        ("todo", "To do"),
        ("in_progress", "In progress"),
        ("done", "Done")
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label="status", required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'media']

        widgets = {
            'content':forms.TextInput(attrs={'class': 'form-control'}),
            'media':forms.FileInput()
        }
