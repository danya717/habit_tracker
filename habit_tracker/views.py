from django.shortcuts import render
from habit_tracker.forms import CreateTaskForm

def top_bar_paths(request):
    form = CreateTaskForm()
    create_task = request.GET.get('create_task')
    path = request.path
    path = path.replace('/', '')
    if path == '':
        path = 'habit_tracker'
    paths = ['Dashboard', 'Create Task', 'Analytics', 'Streaks', 'Settings']
    context = {'paths' : paths, 'create_task' : create_task, 'form' : form}
    return render(request, f'{path}.html', context=context)