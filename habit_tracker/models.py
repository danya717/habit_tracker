from django.db import models

# Create your models here.
class ProfileConfigurationModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.CharField()