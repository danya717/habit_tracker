"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from habit_tracker.views import top_bar_paths, daily_or_weekly_habit_switcher, create_task, get_task, profile_configuration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_task, name='Dashboard'),
    path('create_task', create_task, name='Create Task'),
    path('analytics', top_bar_paths, name='Analytics'),
    path('streaks', top_bar_paths, name='Streaks'),
    path('settings', profile_configuration, name='Settings'),
    path('', daily_or_weekly_habit_switcher, name='Daily Tasks'),
    path('weekly_habits', daily_or_weekly_habit_switcher, name='Weekly Tasks'),
]
