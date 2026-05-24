from django.shortcuts import render
from habit_tracker.forms import CreateTaskForm, ProfileConfigurationForm
from django.shortcuts import redirect

def top_bar_paths(request):
    path = request.path
    path = path.replace('/', '')
    if path == '':
        path = 'habit_tracker'
    paths = ['Dashboard', 'Analytics', 'Streaks', 'Settings']
    context = {'paths' : paths}
    return render(request, f'{path}.html', context=context)

def daily_or_weekly_habit_switcher(request):
    button_path = request.path
    button_path = button_path.replace('/', '')
    if button_path == '':
        button_path = 'habit_tracker'
    button_paths = ['Daily Tasks', 'Weekly Tasks']
    context = {'button_paths' : button_paths}
    return render(request, f'{button_path}.html', context=context)

def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            create_habit = data.get('create_habit')
            create_notes = data.get('create_notes')
            with open('data.csv', 'a') as file:
                file.write(f'{create_habit}|{create_notes}\n')
            # print(data)
            return redirect('Create Task')
        form = CreateTaskForm()
        context = {'form': form}
        return render(request, 'create_task.html', context=context)
    form = CreateTaskForm()
    return render(request, 'create_task.html', {'form': form})

def get_task(request):
    with open('data.csv', 'r') as file:
        data = file.readlines()
        if len(data) > 0:
            task_data_1 = data[-1]
            task_name_1 = task_data_1.split('|')[0]
            task_note_1 = task_data_1.split('|')[0]
        else:
            task_name_1 = ''
            task_note_1 = ''
        context = {'task_name_1': task_name_1, 'task_note_1': task_note_1}
        return render(request, 'habit_tracker.html', context=context)

def profile_configuration(request):
    if request.method == 'POST':
        form = ProfileConfigurationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            bio = data.get('bio')
            with open('data1.csv', 'a') as file:
                file.write(f'{name}|{email}|{bio}\n')
            return redirect('Settings')
    with open('data1.csv', 'r') as file:
        data = file.readlines()
        if len(data) > 0:
            profile_data_1 = data[-1]
            profile_name_1 = profile_data_1.split('|')[0]
            profile_email_1 = profile_data_1.split('|')[1]
            profile_bio_1 = profile_data_1.split('|')[2]
        else:
            profile_name_1 = ''
            profile_email_1 = ''
            profile_bio_1 = ''
    form = ProfileConfigurationForm()
    context = {'form': form, 'profile_name_1': profile_name_1, 'profile_email_1': profile_email_1, 'profile_bio_1': profile_bio_1}
    return render(request, 'settings.html', context=context)
