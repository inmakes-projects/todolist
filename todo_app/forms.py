from dataclasses import fields
from django import forms
from .models import Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'date': forms.TextInput(attrs={'type':'date'})
        }