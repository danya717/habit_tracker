from django.shortcuts import render

def habit_tracker(request):
    return render(request, 'habit_tracker.html')