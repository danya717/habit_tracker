from django import forms

class CreateTaskForm(forms.Form):
    create_task = forms.CharField(max_length=30)