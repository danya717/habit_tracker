from django.shortcuts import render
from habit_tracker.forms import CreateTaskForm
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

def habits(request):
    if request.method == 'GET':
        form = CreateTaskForm()
        return render(request, 'create_task.html', {'form':form})
    elif request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            create_task = data.get('create_task')
            create_notes = data.get('create_notes')
            with open('data.csv', 'a') as file:
                file.write(f'{create_task}|{create_notes}\n')
            print(data)
            return redirect('Create Task')
        else:
            form = CreateTaskForm()
            return render(request, 'create_task.html', {'form':form})