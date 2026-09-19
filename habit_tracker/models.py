from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    bio = models.CharField()

class Streaks(models.Model):
    streak = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Tasks(models.Model):
    task = models.CharField(max_length=40)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=255, default='')

    list_display = ['task', 'note']

    def __str__(self):
        return f'{self.task} | {self.note}'
