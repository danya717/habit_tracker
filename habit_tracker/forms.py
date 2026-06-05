from django import forms

class CreateTaskForm(forms.Form):
    create_habit = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'create_habit_input'}))
    create_notes = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'create_notes_input'}))

class ProfileConfigurationForm(forms.Form):
    name = forms.CharField(max_length=30,  widget=forms.TextInput(attrs={'class': 'name_input'}), label='Full Name')
    birth_date = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'birth_date_input'}), label='Birth Date')
    phone = forms.DateField(widget=forms.TextInput(attrs={'class': 'phone_num_input'}), label='Phone Number')
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'email_input'}), label='Email Address')
    bio = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'bio_input'}), label='Bio')