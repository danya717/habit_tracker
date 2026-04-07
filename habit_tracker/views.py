from django.shortcuts import render

def top_bar_paths(request):
    path = request.path
    path = path.replace('/', '')
    if path == '':
        path = 'habit_tracker'
    paths = ['Dashboard', 'Create Task', 'Analytics', 'Streaks', 'Settings']
    context = {'paths' : paths}
    return render(request, f'{path}.html', context=context)