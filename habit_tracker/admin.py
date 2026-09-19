from django.contrib import admin
from .models import User, Streaks, Tasks

# Register your models here.
admin.site.register(User)
admin.site.register(Streaks)
admin.site.register(Tasks)
