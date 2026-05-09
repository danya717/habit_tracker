from django import forms

class CreateTaskForm(forms.Form):
    create_task = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'create_habit_input'}))
    create_notes = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'create_notes_input'}))