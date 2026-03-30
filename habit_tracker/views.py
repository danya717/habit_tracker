from django.shortcuts import render

def habit_tracker(request):
    return render(request, 'habit_tracker.html')

def my_habits(request):
    return render(request, 'my_habits.html')

def top_bar_paths(request):
    path = request.path
    path = path.replace('/', '')
    if path == '':
        path = 'habit_tracker'
    paths = ['Dashboard', 'My Habits', 'Stats']
    context = {'paths' : paths}
    return render(request, f'{path}.html', context=context)