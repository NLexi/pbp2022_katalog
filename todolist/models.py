from django.conf import settings
from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null = True,
        )
    date = models.DateField(("Date"), default=datetime.date.today)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_finished = models.BooleanField(default=False)