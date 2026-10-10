from django.shortcuts import render
from habit_tracker.forms import CreateTaskForm, ProfileConfigurationForm
from django.shortcuts import redirect
from habit_tracker.models import User, Tasks
from habit_tracker.utils.decorators import call_counter, post_only

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
    context = {'button_paths' : button_paths}
    return render(request, f'{button_path}.html', context=context)

def completed_uncompleted_task_switcher(request):
    path = request.path
    path = path.replace('/', '')
    if path == '':
        path = 'habit_tracker'
    paths = ['Completed Tasks']
    context = {'paths': paths}
    return render(request, f'{path}.html', context=context)

def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            create_task = data.get('task')
            create_notes = data.get('notes')
            Tasks.objects.create(task=create_task, note=create_notes)
            return redirect('Create Task')
    form = CreateTaskForm()
    return render(request, 'create_task.html', {'form': form})

def get_task(request):
    all_tasks = Tasks.objects.filter(is_done=True)
    context = {'all_tasks': all_tasks}
    return render(request, 'habit_tracker.html', context=context)


def profile_configuration(request):
    if request.method == 'POST':
        form = ProfileConfigurationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            birth_date = data.get('birth_date')
            phone = data.get('phone')
            email = data.get('email')
            bio = data.get('bio')
            User.objects.create(name=name, birth_date=birth_date, phone=phone, email=email, bio=bio)
            return redirect('Settings')
    form = ProfileConfigurationForm()
    context = {'form': form}
    return render(request, 'settings.html', context=context)


def view_task_details(request, task_id):
    task = Tasks.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'task_details.html', context)

@post_only
def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('Dashboard')

def mark_task_done(request, task_id):
    Tasks.objects.filter(id=task_id).update(is_done=True)
    return redirect('Dashboard')

