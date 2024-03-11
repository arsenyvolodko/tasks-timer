from django.forms import ModelForm, TextInput

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title'
        ]
